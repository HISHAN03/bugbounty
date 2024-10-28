# Generated by Django 5.1.2 on 2024-10-28 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0003_customadmin_delete_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='customadmin',
            name='email',
            field=models.EmailField(default='placeholder@example.com', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='customadmin',
            name='username',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
