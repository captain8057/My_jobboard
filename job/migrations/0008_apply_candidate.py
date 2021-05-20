# Generated by Django 3.1.1 on 2021-05-20 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0007_auto_20210520_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='Candidate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='apply_job', to=settings.AUTH_USER_MODEL),
        ),
    ]
