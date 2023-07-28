from django.urls import path
from . import views
from .views import UserList
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    # ...
    path('upload/user/excel/', views.upload_user_excel_file, name='upload_user_excel_file'),
    path('upload/company/excel/', views.upload_company_excel_file, name='upload_company_excel_file'),
    path('upload/user/csv/', views.upload_user_csv_file, name='upload_user_csv_file'),
    path('upload/company/csv/', views.upload_company_csv_file, name='upload_company_csv_file'),
    path('api/users/', UserList.as_view(), name='user-list'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # Получение токена
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Обновление токена
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'), # Проверка токена
]
