#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

apt install ffmpeg



python bot.py
