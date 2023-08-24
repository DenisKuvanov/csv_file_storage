import csv
import os

from django import template

register = template.Library()


@register.filter
def filename(path):
    """
    Фильтр для вывода названия файла без абсолютного пути
    """
    return path.split(os.path.sep)[-1]


@register.simple_tag(name='get_headers')
def get_headers(path):
    """
    Тег для получения заголовков таблицы из загруженного csv файла
    """
    with open(path) as cvsfile:
        reader = csv.reader(cvsfile)
        headers = next(reader)

    return headers


@register.simple_tag(name='get_rows')
def get_rows(path):
    """
    Тег для получения списка строк из загруженного csv файла
    """
    with open(path) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        rows = [next(reader) for i in range(20)]

    return rows
