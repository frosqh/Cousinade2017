call myvenv\Scripts\activate
cd Cousinade
python manage.py makemigrations polls
python manage.py sqlmigrate main 0001 &
python manage.py migrate
python manage.py runserver localhost:8000&