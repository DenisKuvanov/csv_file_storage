from django.urls import path

from .views import LoginUser, logout_user, RegisterUser

app_name = 'myauth'

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
]