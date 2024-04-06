cd news
python manage.py makemigrations blog 
python manage.py migrate 
@REM python manage.py createsuperuser 
python manage.py runserver