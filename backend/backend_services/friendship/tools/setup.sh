#!/bin/bash


python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python3 manage.py migrate

exec gunicorn -b 0.0.0.0:8001 project.wsgi:application