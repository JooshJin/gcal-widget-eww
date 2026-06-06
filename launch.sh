#!/bin/bash
eww kill 2>/dev/null
sleep 0.3
GTK_THEME=EwwTransparent eww daemon
sleep 5
eww open calendar
sleep 0.5
WID=$(xdotool search --class "Eww" | tail -1)
wmctrl -i -r "$WID" -b remove,above
wmctrl -i -r "$WID" -b add,below
