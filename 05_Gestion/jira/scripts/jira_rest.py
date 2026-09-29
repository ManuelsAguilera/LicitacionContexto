import json
import os
import sys
import urllib.error
import urllib.request

CLOUD_ID = "b662438c-9aba-4643-a083-82a2fde025f3"
BASE = "https://api.atlassian.com/ex/jira/{}/rest/api/3".format(CLOUD_ID)
AUTH = os.path.join(os.environ["USERPROFILE"], ".local", "share", "opencode", "mcp-auth.json")


def token():
    d = json.load(open(AUTH, encoding="utf-8"))
    return d["jira"]["tokens"]["accessToken"]


def call(method, path, body=None):
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(BASE + path, data=data, method=method)
    req.add_header("Authorization", "Bearer " + token())
    req.add_header("Accept", "application/json")
    if data is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read().decode("utf-8")
            return resp.status, (json.loads(raw) if raw else None)
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", "replace")
        return exc.code, raw


def main():
    cmd = sys.argv[1]
    if cmd == "get":
        status, payload = call("GET", "/issue/{}?fields={}".format(sys.argv[2], sys.argv[3]))
        print(status)
        print(json.dumps(payload, ensure_ascii=False, indent=2)[:1500])
    elif cmd == "labels":
        key = sys.argv[2]
        labels = sys.argv[3:]
        status, payload = call("PUT", "/issue/{}".format(key), {"fields": {"labels": labels}})
        print("PUT labels", key, status, payload if status >= 400 else "OK")
    elif cmd == "delete":
        key = sys.argv[2]
        status, payload = call("DELETE", "/issue/{}".format(key))
        print("DELETE", key, status, payload if status >= 400 else "OK")


if __name__ == "__main__":
    main()
