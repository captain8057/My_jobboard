# Generated by Django 3.1 on 2021-05-17 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210517_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog-img/person.jpg', null=True, upload_to='blog-img/'),
        ),
    ]
