import os
import sys
import django
from datetime import date, timedelta

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mango_pests_project.settings')

django.setup()

from django.contrib.auth.models import User
from mango_pests.models import FarmBlock, PlantType, Pest, PestCheck

admin_user, created = User.objects.get_or_create(username='admin', defaults={
    'email': 'admin@example.com',
    'is_superuser': True,
    'is_staff': True,
})
if created:
    admin_user.set_password('admin')
    admin_user.save()
    print("Admin user created.")
else:
    print("Admin user already exists.")



farm_block, created = FarmBlock.objects.get_or_create(
    grower=admin_user,
    name="Admin's Mango Grove",
    defaults={
        'location_description': 'Test block for demo',
        'stocking_rate': 120,
        'area_hectares': 2.5
    }
)
if created:
    print("FarmBlock created.")
else:
    print("FarmBlock already exists.")


try:
    pest = Pest.objects.get(name__iexact='Anthracnose')
except Pest.DoesNotExist:
    print("Error: Pest 'Anthracnose' does not exist. Seed pest data first.")
    sys.exit(1)


existing_checks = PestCheck.objects.filter(farm_block=farm_block, pest=pest).count()
if existing_checks < 10:
    for i in range(10):
        PestCheck.objects.create(
            farm_block=farm_block,
            pest=pest,
            date_checked=date.today() - timedelta(days=i),
            part_of_plant='Leaves',
            infestation_level='Low',
            num_trees=30 + i * 5,
            positives= int((date.today() - timedelta(days=i)).strftime("%Y%m%d")) % 50,
            notes=f"Seeded record {i+1}",
            path_pattern='ZigZag'
        )
    print("10 PestCheck records created using static pest 'Anthracnose'.")
else:
    print("PestCheck records already exist for this farm block.")
