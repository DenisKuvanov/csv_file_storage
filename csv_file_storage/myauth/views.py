from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from storage_app.views import menu
from .forms import LoginUserForm, RegisterUserForm


# Create your views here.
def logout_user(request: HttpRequest) -> HttpResponse:
    """
    Endpoint для разлогинивания пользователя
    """
    logout(request)
    return redirect('myauth:login')


class RegisterUser(CreateView):
    """
    View endpoint для вывода пользователю страницы для регистрации.
    После успешной валидации, автоматически логинит пользователя
    """
    form_class = RegisterUserForm
    template_name = 'storage_app/register.html'
    success_url = reverse_lazy('myauth:login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Страница регистрации'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('storage_app:home')


class LoginUser(LoginView):
    """
    View endpoint для вывода пользователю страницы для входа на сайт
    """
    form_class = LoginUserForm
    template_name = 'storage_app/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Страница авторизации'
        return context

    # def get_success_url(self):
    #     return reverse_lazy('storage_app:home')
