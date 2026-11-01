#!/usr/bin/env python3
"""Create the Aling33 profile repo if missing, then report its state."""
import json
import os
import subprocess
import urllib.error
import urllib.request

LOGIN = "Aling33"


def creds():
    env = {**os.environ, "GIT_TERMINAL_PROMPT": "0", "GCM_INTERACTIVE": "never"}
    out = subprocess.run(["git", "credential", "fill"], input=f"protocol=https\nhost=github.com\n\n",
                         capture_output=True, text=True, env=env, timeout=30).stdout
    return dict(line.split("=", 1) for line in out.splitlines() if "=" in line)["password"]


TOKEN = creds()


def call(method, url, payload=None):
    req = urllib.request.Request(url, method=method,
                                 data=json.dumps(payload).encode() if payload else None,
                                 headers={"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json",
                                          "User-Agent": LOGIN, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, json.load(r)
    except urllib.error.HTTPError as exc:
        return exc.code, json.loads(exc.read().decode() or "{}")


status, body = call("GET", f"https://api.github.com/repos/{LOGIN}/{LOGIN}")
if status == 404:
    status, body = call("POST", "https://api.github.com/user/repos", {
        "name": LOGIN, "description": "Upstream merged pull request wall", "private": False, "has_issues": False,
        "has_wiki": False, "has_projects": False,
    })
    print("create:", status, body.get("full_name") or body.get("message"))
else:
    print("exists:", status, body.get("full_name"))