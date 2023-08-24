# Generated by Django 4.2.4 on 2023-08-22 18:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import storage_app.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('storage_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv_file',
            name='file',
            field=models.FileField(null=True, upload_to=storage_app.models.csv_file_directory_path, verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='csv_file',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='files', to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
    ]
