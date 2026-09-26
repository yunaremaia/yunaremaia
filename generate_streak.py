#!/usr/bin/env python3
"""Generate a self-hosted contribution streak card for yunaremaia.

Uses GitHub GraphQL API to fetch real contribution data and renders
an SVG that matches the GitHub dark palette. No external service,
no stale cache — always fresh from the API.
"""
import json
import os
import urllib.request
from datetime import datetime, timezone


def main():
    token = os.environ["GH_TOKEN"]
    query = """
    query {
      user(login: "yunaremaia") {
        contributionsCollection {
          contributionCalendar {
            totalContributions
            weeks {
              contributionDays {
                date
                contributionCount
              }
            }
          }
        }
      }
    }
    """
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query}).encode(),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
    )
    resp = urllib.request.urlopen(req, timeout=30)
    data = json.loads(resp.read())
    cal = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    weeks = cal["weeks"]
    all_days = []
    for w in weeks:
        all_days.extend(w["contributionDays"])

    # Current streak
    current = 0
    for d in reversed(all_days):
        if d["contributionCount"] > 0:
            current += 1
        else:
            break

    # Longest streak
    longest = 0
    run = 0
    for d in all_days:
        if d["contributionCount"] > 0:
            run += 1
            longest = max(longest, run)
        else:
            run = 0

    streak_start = all_days[-current]["date"] if current > 0 else "N/A"
    streak_end = all_days[-1]["date"] if current > 0 else "N/A"

    def fmt(d):
        return datetime.strptime(d, "%Y-%m-%d").strftime("%b %d")

    total = cal["totalContributions"]
    W, H = 495, 195
    card_bg, text_primary, text_secondary, accent, divider = (
        "#0D1117", "#E6EDF3", "#8B949E", "#F0883E", "#30363D",
    )
    range_str = f"{fmt(streak_start)} - {fmt(streak_end)}" if current > 0 else "No active streak"

    svg = (
        f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" fill="none" '
        f'xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Contribution streak">\n'
        f'  <style>\n'
        f"    .header {{ font: 600 18px 'Segoe UI', Ubuntu, Sans-Serif; fill: {accent} }}\n"
        f"    .stat {{ font: 600 28px 'Segoe UI', Ubuntu, Sans-Serif; fill: {text_primary} }}\n"
        f"    .label {{ font: 400 14px 'Segoe UI', Ubuntu, Sans-Serif; fill: {text_secondary} }}\n"
        f"    .sub {{ font: 400 12px 'Segoe UI', Ubuntu, Sans-Serif; fill: {text_secondary} }}\n"
        f"    .card {{ fill: {card_bg}; stroke: {divider} }}\n"
        f"  </style>\n"
        f'  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="4.5" class="card"/>\n'
        f'  <text x="25" y="35" class="header">Yunare Maia\'s Contribution Streak</text>\n'
        f'  <text x="25" y="80" class="stat">{total}</text>\n'
        f'  <text x="25" y="100" class="label">Total Contributions</text>\n'
        f'  <text x="180" y="80" class="stat">{current}</text>\n'
        f'  <text x="180" y="100" class="label">Current Streak</text>\n'
        f'  <text x="180" y="118" class="sub">{range_str}</text>\n'
        f'  <text x="340" y="80" class="stat">{longest}</text>\n'
        f'  <text x="340" y="100" class="label">Longest Streak</text>\n'
        f'  <text x="25" y="175" class="sub">Generated {datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")} · self-hosted · always fresh</text>\n'
        f"</svg>"
    )

    with open("streak.svg", "w") as f:
        f.write(svg)
    print(f"streak.svg written: {total} contributions, {current}-day streak, longest {longest}")


if __name__ == "__main__":
    main()
