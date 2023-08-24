from django.urls import path

from .views import Home, FileDetail, AddFile, DeleteFile

app_name = 'storage_app'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('file/<int:pk>/', FileDetail.as_view(), name="file_detail"),
    path('file/add/', AddFile.as_view(), name="add_file"),
    path('file/delete/<int:pk>/', DeleteFile.as_view(), name="delete_file"),
]