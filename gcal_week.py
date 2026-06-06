#!/usr/bin/env python3
"""Outputs week metadata: header label, month/year, and 7-day strip."""
import json
from datetime import date, timedelta

DAYS_KO = ["월", "화", "수", "목", "금", "토", "일"]
DAYS_EN = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
MONTHS_EN = ["January", "February", "March", "April", "May", "June",
             "July", "August", "September", "October", "November", "December"]

today = date.today()
monday = today - timedelta(days=today.weekday())

days = []
for i in range(7):
    d = monday + timedelta(days=i)
    days.append({
        "label": DAYS_EN[i],
        "num": str(d.day),
        "is_today": d == today,
    })

sunday = monday + timedelta(days=6)
if monday.month == sunday.month:
    month_label = f"{MONTHS_EN[monday.month - 1]} {monday.year}"
else:
    month_label = f"{MONTHS_EN[monday.month - 1]}–{MONTHS_EN[sunday.month - 1]} {monday.year}"

print(json.dumps({
    "header": "이번 주",
    "month": month_label,
    "days": days,
}))
