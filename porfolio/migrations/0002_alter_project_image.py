# Generated by Django 3.2.15 on 2022-09-30 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='porfolio/images'),
        ),
    ]
