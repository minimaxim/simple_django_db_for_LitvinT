# urls.py
from django.urls import path
from . import views

app_name = 'bin'


urlpatterns = [
    # ... другие URL-паттерны ...
    path('upload/csv/', views.upload_csv_file, name='upload_csv_file'),
    path('admin/', views.admin_redirect, name='admin_redirect'),
]