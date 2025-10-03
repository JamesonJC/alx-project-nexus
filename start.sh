#!/bin/sh

python manage.py migrate
# python manage.py seed_once
# exec gunicorn jobboard_backend.wsgi:application --bind 0.0.0.0:$PORT

# Start the ASGI server using uvicorn (not gunicorn)
exec uvicorn core.asgi:application --host 0.0.0.0 --port $PORT
