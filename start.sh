#!/bin/sh

python manage.py migrate
# python manage.py seed_once
exec gunicorn jobboard_backend.wsgi:application --bind 0.0.0.0:$PORT