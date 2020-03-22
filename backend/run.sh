#!/bin/sh
gunicorn -w 5 -b 0.0.0.0:5000 app:app&
python3 content_control.py
