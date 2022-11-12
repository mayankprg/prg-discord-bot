#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

sudo apt install ffmpeg



python bot.py
