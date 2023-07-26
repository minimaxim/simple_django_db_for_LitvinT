# urls.py
from django.urls import path
from . import views

app_name = 'bin'

urlpatterns = [
    path('upload/txt/', views.upload_txt_file, name='upload_txt'),
    path('upload/csv/', views.upload_csv_file, name='upload_csv')
]
