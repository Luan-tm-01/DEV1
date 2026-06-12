cd DEV1
pip install -r "requirements.txt"
pip install djangorestframework
python manage.py makemigrations
python manage.py migrate
python wrapper_pessoas.py
python manage.py createsuperuser
python manage.py runserver