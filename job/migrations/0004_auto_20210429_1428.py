# Generated by Django 3.1.1 on 2021-04-29 11:28

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_job_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='Country',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='Place',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]