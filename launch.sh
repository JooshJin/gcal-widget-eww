#!/bin/bash
eww kill 2>/dev/null
sleep 0.3
GTK_THEME=Adwaita eww daemon
sleep 5
eww open calendar
sleep 0.3
xdotool search --class "Eww" windowlower
