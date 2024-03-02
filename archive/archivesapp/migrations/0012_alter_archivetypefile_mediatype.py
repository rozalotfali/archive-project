# Generated by Django 5.0.2 on 2024-02-21 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archivesapp', '0011_remove_archivetypefile_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivetypefile',
            name='mediatype',
            field=models.CharField(blank=True, choices=[('F', 'File'), ('A', 'Audio'), ('T', 'Text'), ('P', 'Picture'), ('V', 'Video')], max_length=1, null=True),
        ),
    ]