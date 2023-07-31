from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views
from .views import ProtectedViewUser, ProtectedViewCompany, LoginUserView

urlpatterns = [
    path('upload/user/excel/', views.upload_user_excel_file, name='upload_user_excel_file'),
    path('upload/company/excel/', views.upload_company_excel_file, name='upload_company_excel_file'),
    path('upload/user/csv/', views.upload_user_csv_file, name='upload_user_csv_file'),
    path('upload/company/csv/', views.upload_company_csv_file, name='upload_company_csv_file'),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/users/', ProtectedViewUser.as_view(), name='protected_view_user'),
    path('api/v1/companies/', ProtectedViewCompany.as_view(), name='protected_view_company'),
    path('', LoginUserView.as_view(), name='index'),
]
