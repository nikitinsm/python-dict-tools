#!/usr/bin/env bash
# pip install watchdog to get ability of watchmedo
# pip install nose to get ability of nosetests
watchmedo shell-command --recursive -p "*.py" -c "nosetests --nocapture" --interval=30 --drop ./