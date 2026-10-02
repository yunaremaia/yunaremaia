#!/usr/bin/env python3
"""Tests for generate_streak.py.

These drive the real ``main()`` entry point with a stubbed network layer, so
they exercise the streak maths and the SVG it renders rather than a refactored
re-implementation of it.

No third-party dependencies: run with ``python3 -m unittest discover -s tests``.
"""
import contextlib
import io
import json
import os
import shutil
import sys
import tempfile
import unittest
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import generate_streak  # noqa: E402


def day(date, count):
    return {"date": date, "contributionCount": count}


def response(days, total=None):
    """A GitHub GraphQL payload for a flat list of contribution days."""
    payload = {
        "data": {
            "user": {
                "contributionsCollection": {
                    "contributionCalendar": {
                        "totalContributions": total if total is not None else sum(
                            d["contributionCount"] for d in days
                        ),
                        "weeks": [{"contributionDays": days}],
                    }
                }
            }
        }
    }
    return json.dumps(payload).encode()


class StreakTestCase(unittest.TestCase):
    """Runs main() against a stubbed API in a throwaway directory."""

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmpdir, ignore_errors=True)
        self._cwd = os.getcwd()
        os.chdir(self.tmpdir)
        self.addCleanup(os.chdir, self._cwd)

        token = os.environ.get("GH_TOKEN")
        os.environ["GH_TOKEN"] = "test-token"
        if token is None:
            self.addCleanup(os.environ.pop, "GH_TOKEN", None)

        self._real_urlopen = urllib.request.urlopen
        self.addCleanup(setattr, urllib.request, "urlopen", self._real_urlopen)

    def run_main(self, body):
        """Run main() with the API returning ``body``, return its stdout."""
        urllib.request.urlopen = lambda req, timeout=None: io.BytesIO(body)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            generate_streak.main()
        return buf.getvalue()

    def svg(self):
        with open(os.path.join(self.tmpdir, "streak.svg")) as fh:
            return fh.read()


class TestHappyPath(StreakTestCase):
    def test_writes_streak_svg(self):
        self.run_main(response([day("2026-10-01", 1), day("2026-10-02", 2)]))
        self.assertTrue(os.path.exists(os.path.join(self.tmpdir, "streak.svg")))

    def test_reports_totals_on_stdout(self):
        out = self.run_main(response([day("2026-10-01", 1), day("2026-10-02", 2)]))
        self.assertIn("streak.svg written", out)
        self.assertIn("3 contributions", out)  # 1 + 2
        self.assertIn("2-day streak", out)

    def test_svg_is_well_formed_xml(self):
        from xml.etree import ElementTree

        self.run_main(response([day("2026-10-01", 1), day("2026-10-02", 2)]))
        ElementTree.fromstring(self.svg())  # raises on malformed markup

    def test_total_contributions_comes_from_the_api(self):
        # The API's own total must win over a re-derivation from the days.
        self.run_main(response([day("2026-10-01", 1), day("2026-10-02", 2)], total=999))
        self.assertIn("999", self.svg())


class TestCurrentStreak(StreakTestCase):
    def test_counts_trailing_consecutive_days(self):
        days = [
            day("2026-09-01", 0),
            day("2026-09-02", 3),
            day("2026-09-03", 0),
            day("2026-09-04", 1),
            day("2026-09-05", 4),
        ]
        out = self.run_main(response(days))
        self.assertIn("2-day streak", out)

    def test_zero_when_latest_day_is_empty(self):
        days = [day("2026-09-01", 5), day("2026-09-02", 0)]
        out = self.run_main(response(days))
        self.assertIn("0-day streak", out)

    def test_whole_range_when_every_day_counts(self):
        days = [day("2026-09-0%d" % i, 1) for i in range(1, 6)]
        out = self.run_main(response(days))
        self.assertIn("5-day streak", out)

    def test_no_active_streak_when_nothing_counts(self):
        out = self.run_main(response([day("2026-09-01", 0), day("2026-09-02", 0)]))
        self.assertIn("0-day streak", out)
        self.assertIn("No active streak", self.svg())


class TestLongestStreak(StreakTestCase):
    def test_finds_a_run_in_the_middle(self):
        days = [
            day("2026-09-01", 1),
            day("2026-09-02", 1),
            day("2026-09-03", 1),
            day("2026-09-04", 0),
            day("2026-09-05", 1),
        ]
        out = self.run_main(response(days))
        self.assertIn("longest 3", out)

    def test_longer_historical_run_beats_the_current_one(self):
        days = [day("2026-09-0%d" % i, 1) for i in range(1, 5)] + [
            day("2026-09-05", 0),
            day("2026-09-06", 1),
        ]
        out = self.run_main(response(days))
        self.assertIn("longest 4", out)

    def test_empty_day_does_not_count_toward_the_longest_run(self):
        # Guards a run counter that is seeded with 1 instead of reset to 0:
        # a leading zero day would be absorbed and the run inflated by one.
        days = [day("2026-09-01", 0), day("2026-09-02", 1)]
        out = self.run_main(response(days))
        self.assertIn("longest 1", out)

    def test_trailing_empty_day_does_not_inflate_the_run(self):
        days = [day("2026-09-01", 1), day("2026-09-02", 0)]
        out = self.run_main(response(days))
        self.assertIn("longest 1", out)

    def test_zero_when_no_day_counts(self):
        out = self.run_main(response([day("2026-09-01", 0)]))
        self.assertIn("longest 0", out)


class TestCalendarEdgeCases(StreakTestCase):
    def test_empty_calendar_renders(self):
        # No weeks at all: nothing to count, but it must still not crash.
        out = self.run_main(response([]))
        self.assertIn("streak.svg written", out)
        self.assertIn("No active streak", self.svg())

    def test_single_day_calendar(self):
        out = self.run_main(response([day("2026-09-01", 7)]))
        self.assertIn("1-day streak", out)
        self.assertIn("Sep 01", self.svg())

    def test_multi_week_calendar_is_flattened(self):
        # Weeks arrive as separate buckets; days must be joined end to end.
        payload = json.dumps(
            {
                "data": {
                    "user": {
                        "contributionsCollection": {
                            "contributionCalendar": {
                                "totalContributions": 2,
                                "weeks": [
                                    {"contributionDays": [day("2026-09-01", 1)]},
                                    {"contributionDays": [day("2026-09-02", 1)]},
                                ],
                            }
                        }
                    }
                }
            }
        ).encode()
        out = self.run_main(payload)
        self.assertIn("2-day streak", out)  # the 0-contribution gap is absent


class TestSvgContent(StreakTestCase):
    def test_date_range_is_rendered_for_an_active_streak(self):
        days = [day("2026-09-01", 1), day("2026-09-02", 1)]
        self.run_main(response(days))
        self.assertIn("Sep 01 - Sep 02", self.svg())

    def test_card_carries_expected_dimensions(self):
        self.run_main(response([day("2026-09-01", 1)]))
        self.assertIn('width="495"', self.svg())
        self.assertIn('height="195"', self.svg())


if __name__ == "__main__":
    unittest.main()