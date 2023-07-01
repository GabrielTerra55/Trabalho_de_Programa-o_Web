pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput
python3.9 manage.py migrate

echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@admin.com', '40028922')" | python manage.py shell