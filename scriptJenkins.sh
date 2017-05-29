#!/bin/bash
source last-minute-env/bin/activate
cd Cousinade/
#fuser 8888/tcp -k
#pip install -r requirements.txt
python manage.py makemigrations polls
#python manage.py check --deploy
python manage.py sqlmigrate polls 0001 &
python manage.py migrate
#python manage.py test
BUILD_ID=dontKillMe python manage.py runserver localhost:8888 &
