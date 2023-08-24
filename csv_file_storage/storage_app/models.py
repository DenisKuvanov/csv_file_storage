import re

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
import os

from django.urls import reverse


def csv_file_directory_path(instance: "CSV_file", filename: str) -> str:
    """
    Функция для написания пити для хранения файла пользователя
    """
    return "user_{pk}/files/{filename}".format(
        pk=instance.owner.pk,
        filename=filename
    )

class CSV_file(models.Model):
    """
    Django модель, которая представляет собой загружаемый файл пользователя

    owner: владелец файла
    file: сам файл
    created_at: время загрузки файла
    """
    class Meta:
        ordering = ['pk']
        verbose_name_plural = 'CSV_files'
        verbose_name = "CSV_file"

    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name='files', verbose_name="Владелец")
    file = models.FileField(null=True, upload_to=csv_file_directory_path, verbose_name='Файл')
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('storage_app:file_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.file.name.split(os.path.sep)[-1]

    def clean(self):
        pattern = re.compile(r'.*\.csv$')

        if not pattern.search(self.file.name):
            raise ValidationError('Only .csv files are accepted')