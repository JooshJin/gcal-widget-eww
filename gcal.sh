#!/bin/bash
gcalcli --config-folder ~/.config/gcalcli --conky --lineart=ascii calw --monday --nocolor 2>/dev/null | sed 's/\${color[^}]*}//g'
