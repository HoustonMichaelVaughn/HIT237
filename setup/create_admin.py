import os
import sys
import django


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


sys.path.insert(0, BASE_DIR)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mango_pests_project.settings')
django.setup()

from django.contrib.auth.models import User

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    print("Admin user created.")
else:
    print("Admin user already exists.")
