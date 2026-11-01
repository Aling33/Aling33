#!/usr/bin/env python3
"""Regenerate the profile README block and the merged-PR wall SVG.

Usage: python scripts/update_prs.py README.md <login>
Needs GITHUB_TOKEN to stay inside the API rate limit.
"""
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

README = sys.argv[1] if len(sys.argv) > 1 else "README.md"
LOGIN = sys.argv[2] if len(sys.argv) > 2 else os.environ["GITHUB_REPOSITORY_OWNER"]
TOKEN = os.environ.get("GITHUB_TOKEN", "")
START, END = "<!-- upstream-prs:start -->", "<!-- upstream-prs:end -->"
SVG = os.path.join(os.path.dirname(os.path.abspath(README)), "merged-prs.svg")
CACHE = os.path.join(os.path.dirname(os.path.abspath(README)), "stars.json")


def api(url):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": LOGIN}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    # large responses truncate on flaky links
    for attempt in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=60) as resp:
                return json.load(resp)
        except urllib.error.HTTPError:
            raise
        except Exception:
            if attempt == 2:
                raise
            time.sleep(2 * (attempt + 1))


def fetch_prs():
    # -user: drops PRs against the user's own repos, which are noise on a profile
    q = urllib.parse.quote(f"is:pr author:{LOGIN} -user:{LOGIN}")
    prs, page = [], 1
    while True:
        data = api(f"https://api.github.com/search/issues?q={q}&per_page=100&page={page}&sort=updated")
        items = data.get("items") or []
        for it in items:
            pr = it["pull_request"]
            state = "✅ merged" if pr.get("merged_at") else ("🟡 open" if it["state"] == "open" else "⚪ closed")
            prs.append({"repo": it["repository_url"].split("/repos/", 1)[1], "n": it["number"],
                        "title": " ".join(it["title"].split()), "url": it["html_url"],
                        "state": state, "date": it["created_at"][:10]})
        if not items or page >= 10 or page * 100 >= data.get("total_count", 0):
            return prs
        page += 1


def fetch_stars(repos):
    try:
        cached = {r["repo"]: r["stars"] for r in json.load(open(CACHE, encoding="utf-8"))}
    except Exception:
        cached = {}
    stars = {}
    for repo in repos:
        try:
            stars[repo] = api(f"https://api.github.com/repos/{repo}").get("stargazers_count", 0)
            time.sleep(0.2)
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                stars[repo] = 0
            else:  # rate limited: fall back to the numbers from the last local run
                return {**cached, **stars}
    return stars


def fmt(n):
    return f"{n / 1000:.1f}".rstrip("0").rstrip(".") + "k" if n >= 1000 else str(n)


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


DARK, WHITE, BORDER, ALT, MUTED, LINK = "#2d333b", "#ffffff", "#d0d7de", "#f6f8fa", "#57606a", "#0969da"


def render_svg(rows, path):
    """rows: [(repo, merged, stars)] already sorted."""
    W, PAD, H = 880, 24, 46
    top, head = 16, 44
    height = top + 56 + 22 + head + H * len(rows) + 24
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{height}" viewBox="0 0 {W} {height}" '
         f'font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif">',
         f'<rect width="{W}" height="{height}" fill="{WHITE}"/>']

    pw = (W - 2 * PAD - 24) / 3
    for i, (label, value, color) in enumerate([
        ("MERGED PRS", str(sum(r[1] for r in rows)), "#8250df"),
        ("PROJECTS", str(len(rows)), "#0969da"),
        ("UPSTREAM ★", fmt(sum(r[2] for r in rows)), "#bc4c00"),
    ]):
        x, lw = PAD + i * (pw + 12), pw * 0.72
        o += [f'<rect x="{x:.1f}" y="{top}" width="{lw:.1f}" height="56" rx="6" fill="{DARK}"/>',
              f'<text x="{x + 14:.1f}" y="{top + 33:.1f}" fill="#fff" font-size="13" font-weight="700" letter-spacing="0.5">{label}</text>',
              f'<rect x="{x + lw:.1f}" y="{top}" width="{pw - lw:.1f}" height="56" rx="6" fill="{color}"/>',
              f'<text x="{x + lw + (pw - lw) / 2:.1f}" y="{top + 35:.1f}" fill="#fff" font-size="19" font-weight="800" text-anchor="middle">{value}</text>']

    ty, tw = top + 56 + 22, W - 2 * PAD
    cx, cs, cm = PAD + 24, PAD + tw * 0.62, PAD + tw * 0.88
    o.append(f'<rect x="{PAD}" y="{ty}" width="{tw}" height="{head}" fill="{WHITE}" stroke="{BORDER}"/>')
    for tx, anchor, label in ((cx, "start", "Project"), (cs, "middle", "★ Stars"), (cm, "middle", "Merged")):
        o.append(f'<text x="{tx:.1f}" y="{ty + head / 2 + 6:.1f}" fill="#24292f" font-size="16" font-weight="700" text-anchor="{anchor}">{label}</text>')

    for i, (repo, merged, stars) in enumerate(rows):
        ry = ty + head + i * H
        o += [f'<rect x="{PAD}" y="{ry}" width="{tw}" height="{H}" fill="{ALT if i % 2 else WHITE}" stroke="{BORDER}"/>',
              f'<text x="{cx:.1f}" y="{ry + H / 2 + 6:.1f}" fill="{LINK}" font-size="15" font-weight="500">{esc(repo)}</text>',
              f'<text x="{cs:.1f}" y="{ry + H / 2 + 6:.1f}" fill="#24292f" font-size="15" text-anchor="middle">{fmt(stars)}</text>',
              f'<text x="{cm:.1f}" y="{ry + H / 2 + 6:.1f}" fill="#24292f" font-size="15" text-anchor="middle">{merged}</text>']

    o += [f'<text x="{PAD}" y="{height - 8}" fill="{MUTED}" font-size="11">Updated '
          f'{datetime.now(timezone.utc):%Y-%m-%d} · via GitHub Actions · @{LOGIN}</text>', "</svg>"]
    open(path, "w", encoding="utf-8", newline="\n").write("\n".join(o))


prs = fetch_prs()
by_repo = {}
for p in prs:
    by_repo.setdefault(p["repo"], []).append(p)
for v in by_repo.values():
    v.sort(key=lambda p: p["date"], reverse=True)

stars = fetch_stars(sorted(by_repo))
merged_of = lambda repo: sum(p["state"].startswith("✅") for p in by_repo[repo])
wall = [(r, merged_of(r), stars.get(r, 0)) for r in by_repo if merged_of(r)]
wall.sort(key=lambda r: (-r[2], -r[1], r[0]))
render_svg(wall, SVG)

total = len(prs)
merged = sum(merged_of(r) for r in by_repo)

# the README stays a single image; the per-PR detail lives in its own page
lines = [f"# 上游 PR 清单", "", f"共 **{total}** 个 PR，覆盖 **{len(by_repo)}** 个上游项目，**{merged}** 个已合并。", ""]
for repo in sorted(by_repo, key=lambda r: (-merged_of(r), -len(by_repo[r]), r.lower())):
    lines += [f"<details><summary><b>{repo}</b> — {len(by_repo[repo])} PR / {merged_of(repo)} merged</summary>", ""]
    lines += [f"- `{p['date']}` [#{p['n']}]({p['url']}) {p['title']} — {p['state']}" for p in by_repo[repo]]
    lines += ["", "</details>", ""]
open(os.path.join(os.path.dirname(os.path.abspath(README)), "PRS.md"), "w",
     encoding="utf-8", newline="\n").write("\n".join(lines).rstrip() + "\n")

text = open(README, encoding="utf-8").read()
new = re.sub(re.escape(START) + r".*?" + re.escape(END), f"{START}\n![Merged PR Wall](merged-prs.svg)\n{END}",
             text, flags=re.S)
if new != text:
    open(README, "w", encoding="utf-8", newline="\n").write(new)
print(f"wall: {merged} merged PRs over {len(wall)} projects; readme {'updated' if new != text else 'unchanged'}")