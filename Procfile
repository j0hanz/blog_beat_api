release: python manage.py makemigrations && python manage.py migrate
web: gunicorn blog_beat_api.wsgi