from django.urls import path
from . import views

urlpatterns = [
    # ...
    path('upload/user/excel/', views.upload_user_excel_file, name='upload_user_excel_file'),
    path('upload/company/excel/', views.upload_company_excel_file, name='upload_company_excel_file'),
    path('upload/user/csv/', views.upload_user_csv_file, name='upload_user_csv_file'),
    path('upload/company/csv/', views.upload_company_csv_file, name='upload_company_csv_file'),
]
