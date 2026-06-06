#!/usr/bin/env python3
import subprocess
import json
import re
from datetime import date, timedelta

today = date.today()
monday = today - timedelta(days=today.weekday())
next_monday = monday + timedelta(days=7)

result = subprocess.run(
    [
        "gcalcli",
        "--config-folder", "/home/joosh/.config/gcalcli",
        "agenda",
        monday.strftime("%Y-%m-%d"),
        next_monday.strftime("%Y-%m-%d"),
    ],
    capture_output=True,
    text=True,
)

ansi_escape = re.compile(r'\x1b\[[0-9;]*m')
clean = ansi_escape.sub('', result.stdout)

events = []
current_date = ""
for line in clean.splitlines():
    # Line with date prefix: "Mon Jun 08  7:00pm  Title"
    m = re.match(r'(\w{3} \w{3}\s+\d{1,2})\s+(\d{1,2}:\d{2}(?:am|pm)|All Day)\s+(.+)', line)
    if m:
        current_date = m.group(1).strip()
        events.append({"date": current_date, "time": m.group(2), "title": m.group(3).strip()})
        continue
    # Continuation line (same day, indented)
    m2 = re.match(r'\s{10,}(\d{1,2}:\d{2}(?:am|pm)|All Day)\s+(.+)', line)
    if m2 and current_date:
        events.append({"date": current_date, "time": m2.group(1), "title": m2.group(2).strip()})

print(json.dumps(events))
