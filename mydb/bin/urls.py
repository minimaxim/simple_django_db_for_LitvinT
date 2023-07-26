# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_txt_file, name='upload_txt_file'),
]
