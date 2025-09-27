#!/bin/bash

cd jobboard_backend
python manage.py collectstatic --noinput
python manage.py migrate
gunicorn core.wsgi:application
