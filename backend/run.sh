#!/bin/sh
python3 telegram_bot.py&
gunicorn -w 5 -b 0.0.0.0:5000 app:app
