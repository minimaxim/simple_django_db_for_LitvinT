from django.urls import path
from . import views
from .views import UserList
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import CustomTokenObtainPairView, CustomProtectedView
from .views import ProtectedView


urlpatterns = [
    path('upload/user/excel/', views.upload_user_excel_file, name='upload_user_excel_file'),
    path('upload/company/excel/', views.upload_company_excel_file, name='upload_company_excel_file'),
    path('upload/user/csv/', views.upload_user_csv_file, name='upload_user_csv_file'),
    path('upload/company/csv/', views.upload_company_csv_file, name='upload_company_csv_file'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/protected/', ProtectedView.as_view(), name='protected_view'),
]


