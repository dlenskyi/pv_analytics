#!/bin/sh
virtualenv -p python3 .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python manage.py migrate
.venv/bin/python manage.py collectstatic --noinput
.venv/bin/python manage.py createsuperuser --noinput
.venv/bin/python manage.py compilemessages --ignore .venv
