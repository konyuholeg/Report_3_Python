
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tracker", "0003_profile_skills_length"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]
