# Generated by Django 3.1 on 2021-05-17 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210517_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='blog-img/blog-def-img.png', upload_to='blog-img/'),
        ),
    ]