# Generated by Django 5.0.2 on 2024-02-20 09:22

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_custommanager_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Custommanager',
        ),
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='lastname',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
