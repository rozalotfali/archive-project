# Generated by Django 5.0.2 on 2024-02-21 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archivesapp', '0008_remove_archivetypefile_fileupload_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='archivetypefile',
            old_name='filetype',
            new_name='Mediatype',
        ),
    ]
