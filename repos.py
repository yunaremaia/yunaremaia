import json, os, sys, traceback
sys.path.insert(0, "."); os.environ["GH_TOKEN"] = "dummy"
import generate_streak

class Resp:
    def read(self):
        return json.dumps({"data": None, "errors": [
            {"type": "NOT_FOUND",
             "message": "Could not resolve to a User with the login of 'yunaremaia'."}]}).encode()

generate_streak.urllib.request.urlopen = lambda req, timeout=None: Resp()
try:
    generate_streak.main()
except Exception:
    traceback.print_exc()