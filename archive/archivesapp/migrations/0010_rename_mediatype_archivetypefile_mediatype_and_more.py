# Generated by Django 5.0.2 on 2024-02-21 13:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archivesapp', '0009_rename_filetype_archivetypefile_mediatype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='archivetypefile',
            old_name='Mediatype',
            new_name='mediatype',
        ),
        migrations.AddField(
            model_name='archivetypefile',
            name='media',
            field=models.FileField(blank=True, null=True, upload_to='media/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['file', 'pic', 'audio', 'text', 'video'])]),
        ),
    ]
