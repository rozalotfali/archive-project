# Generated by Django 5.0.2 on 2024-02-21 10:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archivesapp', '0005_remove_archivetypefile_audio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivetypefile',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='audio_files/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'WAV', 'VMA'])]),
        ),
        migrations.AddField(
            model_name='archivetypefile',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
        migrations.AddField(
            model_name='archivetypefile',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='archivetypefile',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='vidio/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'mkv'])]),
        ),
        migrations.AlterField(
            model_name='archivetypefile',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'html', 'xml', 'csv'])]),
        ),
    ]
