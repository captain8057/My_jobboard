# Generated by Django 3.1.1 on 2021-05-05 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_auto_20210429_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='Dead_line',
            field=models.DateTimeField(null=True),
        ),
    ]
