import csv

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.core.paginator import Paginator

from .models import CSV_file
from .forms import AddFileForm

menu = [{'title': "Главная страница", 'url_name': 'storage_app:home'},
        {'title': "Добавить новый файл", 'url_name': 'storage_app:add_file'},
        ]


class Home(ListView):
    """
    View, которая выводит на страницу список загруженных пользователями файлов.
    У каждого файла отображается имя владельца, дата загрузки, название и список заголовков.
    """
    model = CSV_file
    template_name = 'storage_app/index.html'
    context_object_name = 'files'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        return context


class FileDetail(DetailView):
    """
    View для вывода содержимого csv файла
    """
    model = CSV_file
    template_name = 'storage_app/file_detail.html'
    context_object_name = 'file'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        rows = self.get_rows()
        paginator = Paginator(rows, 15)

        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context['menu'] = menu
        context['title'] = 'Информация о файле'
        context['page_obj'] = page_obj
        context['paginator'] = paginator
        return context

    def get_rows(self):
        path = self.object.file.path
        with open(path) as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            rows = [row for row in reader]

        return rows


class AddFile(LoginRequiredMixin, View):
    """
    View для добавления нового csv файла
    """

    def get(self, request: HttpRequest):
        form = AddFileForm()
        context = {
            'title': 'Загрузка нового файла',
            'menu': menu,
            'form': form,
        }
        return render(request, 'storage_app/add_file.html', context=context)

    def post(self, request: HttpRequest):
        form = AddFileForm(request.POST, request.FILES)
        if form.is_valid():
            owner = request.user
            form.cleaned_data['owner'] = owner
            file = CSV_file.objects.create(**form.cleaned_data)
            return redirect(file.get_absolute_url())

        context = {
            'title': 'Загрузка нового файла',
            'menu': menu,
            'form': form,
        }
        return render(request, 'storage_app/add_file.html', context=context)


class DeleteFile(DeleteView):
    """
    View для удаления csv файла пользователя
    """
    model = CSV_file
    context_object_name = 'file'
    success_url = reverse_lazy("storage_app:home")
    template_name = 'storage_app/delete_file.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление файла'
        context['menu'] = menu
        return context
