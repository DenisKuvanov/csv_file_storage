import re

from django import forms
from django.core.exceptions import ValidationError


def validate_file(file):
    """
    Валидатор, который проверяет, что загружаемый файл имеет расширение .csv
    """
    pattern = re.compile(r'.*\.csv$')

    if not pattern.search(file.name):
        raise ValidationError('Для загрузки доступны только .csv файлы')


class AddFileForm(forms.Form):
    """
    Django форма для добавления файла csv
    """
    file = forms.FileField(label='Файл', validators=[validate_file])



