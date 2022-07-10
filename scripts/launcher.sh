#!/bin/bash
# launcher.sh

PYTHONPATH="/usr/lib/python3.9"
PROJECT_DIR="/home/pi/indihome-logger"

cd $PROJECT_DIR

# Activate venv
. $PROJECT_DIR/venv/bin/activate

sudo python3 main.py > $PROJECT_DIR/logs/error.log 2>&1 &

