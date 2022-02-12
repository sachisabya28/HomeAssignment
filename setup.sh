#!/bin/bash

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python manage.py makemigrations
python manage.py migrate