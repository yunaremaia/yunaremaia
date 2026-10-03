#!/usr/bin/env python3
"""Tests for generate_streak.py's failure reporting.

generate_streak.py used to fail blind: a missing GH_TOKEN raised a bare
``KeyError``, an HTTP failure surfaced as an ``HTTPError`` traceback, and a
GraphQL ``errors`` payload fell through to a ``KeyError`` on the missing
``data`` key. Each of those fails with output that does not tell you what to
do next.

These tests drive the real ``main()`` with the network stubbed and assert on
the exit message, because the message *is* the feature.
"""
import contextlib
import io
import json
import os
import shutil
import sys
import tempfile
import unittest
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import generate_streak  # noqa: E402


class ErrorReportingTestCase(unittest.TestCase):
    """Runs main() in a throwaway directory and captures its exit message."""

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmpdir, ignore_errors=True)
        self._cwd = os.getcwd()
        os.chdir(self.tmpdir)
        self.addCleanup(os.chdir, self._cwd)

        self._real_urlopen = urllib.request.urlopen
        self.addCleanup(setattr, urllib.request, "urlopen", self._real_urlopen)

        # A token is present by default so that each test isolates the failure
        # it is about; the missing-token tests clear it explicitly.
        self._real_token = os.environ.get("GH_TOKEN")
        os.environ["GH_TOKEN"] = "test-token"
        if self._real_token is None:
            self.addCleanup(os.environ.pop, "GH_TOKEN", None)
        else:
            self.addCleanup(os.environ.__setitem__, "GH_TOKEN", self._real_token)

    def run_main(self, urlopen):
        """Run main() with ``urlopen`` as the network layer, return the message.

        Returns the SystemExit message. Fails the test if main() does not
        exit -- these paths must not fall through to a successful run.
        """
        urllib.request.urlopen = urlopen
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            with self.assertRaises(SystemExit) as caught:
                generate_streak.main()
        return str(caught.exception)


class TestMissingToken(ErrorReportingTestCase):
    def test_absent_token_names_the_variable(self):
        token = os.environ.pop("GH_TOKEN", None)
        self.addCleanup(os.environ.__setitem__, "GH_TOKEN", token)
        os.environ["GH_TOKEN"] = ""

        msg = self.run_main(lambda req, timeout=None: io.BytesIO(b"{}"))
        self.assertIn("GH_TOKEN", msg)

    def test_absent_token_does_not_raise_keyerror(self):
        # The pre-fix behaviour was os.environ["GH_TOKEN"] -> KeyError,
        # which prints the variable name but no explanation of the fix.
        token = os.environ.pop("GH_TOKEN", None)
        self.addCleanup(os.environ.__setitem__, "GH_TOKEN", token)

        with contextlib.redirect_stderr(io.StringIO()):
            msg = self.run_main(lambda req, timeout=None: io.BytesIO(b"{}"))
        self.assertNotIn("KeyError", msg)
        self.assertIn("read:user", msg)


class TestHttpFailure(ErrorReportingTestCase):
    def _raise(self, exc):
        # HTTPError wraps its file object in a temporary-file closer that
        # warns on deallocation, so close it explicitly for clean output.
        # URLError has no such file object and no close().
        if hasattr(exc, "close"):
            self.addCleanup(exc.close)

        def urlopen(req, timeout=None):
            raise exc

        return urlopen

    def test_http_error_reports_the_status_code(self):
        exc = urllib.error.HTTPError(
            "https://api.github.com/graphql", 401, "Bad credentials", {}, io.BytesIO()
        )
        msg = self.run_main(self._raise(exc))
        self.assertIn("401", msg)
        self.assertIn("Bad credentials", msg)

    def test_http_error_does_not_leak_a_traceback(self):
        exc = urllib.error.HTTPError(
            "https://api.github.com/graphql", 403, "rate limit exceeded", {}, io.BytesIO()
        )
        with contextlib.redirect_stderr(io.StringIO()):
            msg = self.run_main(self._raise(exc))
        self.assertNotIn("Traceback", msg)
        self.assertNotIn("urllib.error", msg)

    def test_unreachable_host_reports_the_reason(self):
        msg = self.run_main(
            self._raise(urllib.error.URLError("Name or service not known"))
        )
        self.assertIn("api.github.com", msg)
        self.assertIn("Name or service not known", msg)


class TestGraphQLErrors(ErrorReportingTestCase):
    def _payload(self, errors):
        return json.dumps({"data": None, "errors": errors}).encode()

    def test_graphql_error_message_is_surfaced(self):
        msg = self.run_main(
            lambda req, timeout=None: io.BytesIO(
                self._payload([{"message": "Field 'nope' doesn't exist"}])
            )
        )
        self.assertIn("Field 'nope' doesn't exist", msg)

    def test_multiple_graphql_errors_are_all_reported(self):
        msg = self.run_main(
            lambda req, timeout=None: io.BytesIO(
                self._payload([{"message": "first problem"}, {"message": "second problem"}])
            )
        )
        self.assertIn("first problem", msg)
        self.assertIn("second problem", msg)

    def test_error_entry_without_a_message_still_reports(self):
        # A malformed entry must not raise inside the formatter itself --
        # that would replace a useful error with a traceback.
        msg = self.run_main(
            lambda req, timeout=None: io.BytesIO(
                self._payload([{"type": "NOT_FOUND"}])
            )
        )
        self.assertIn("NOT_FOUND", msg)

class _Resp:
    """Fake response whose read() returns bytes or raises."""
    def __init__(self, body=b"", exc=None):
        self._body, self._exc = body, exc

    def read(self):
        if self._exc:
            raise self._exc
        return self._body

class TestTimeout(ErrorReportingTestCase):
    def test_timeout_while_waiting_for_headers(self):
        def urlopen(req, timeout=None):
            raise TimeoutError("timed out")

        msg = self.run_main(urlopen)
        self.assertIn("Timed out", msg)
        self.assertIn("api.github.com", msg)
    def test_timeout_while_reading_the_body(self):
        # urlopen() succeeds, then the socket stalls inside read().
        msg = self.run_main(
            lambda req, timeout=None: _Resp(exc=TimeoutError("timed out"))
        )
        self.assertIn("Timed out", msg)

class TestNonJsonBody(ErrorReportingTestCase):
    def test_html_error_page(self):
        msg = self.run_main(
            lambda req, timeout=None: _Resp(b"<html>502 Bad Gateway</html>")
        )
        self.assertIn("non-JSON", msg)

    def test_empty_body(self):
        msg = self.run_main(lambda req, timeout=None: _Resp(b""))
        self.assertIn("non-JSON", msg)

class TestMissingUser(ErrorReportingTestCase):
    def _run(self, payload):
        return self.run_main(
            lambda req, timeout=None: _Resp(json.dumps(payload).encode())
        )

    def test_user_is_null(self):
        self.assertIn("no user data", self._run({"data": {"user": None}}))

    def test_data_is_null(self):
        self.assertIn("no user data", self._run({"data": None}))

    def test_data_key_absent(self):
        self.assertIn("no user data", self._run({}))

if __name__ == "__main__":
    unittest.main()
