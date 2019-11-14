from django.urls import path
from rest_framework.authtoken import views
from .views import UserCreateAPIView, UserUpdateAPIView, UserListAPIView, UserDetailAPIView


urlpatterns = [
    path('', UserListAPIView.as_view(), name='user_list_url'),
    path('<int:id>/', UserDetailAPIView.as_view(), name='user_detail_url'),
    path('create/', UserCreateAPIView.as_view(), name='user_create_url'),
    path('<int:id>/update/', UserUpdateAPIView.as_view(), name='user_update_url'),
    path('token-auth/', views.obtain_auth_token, name='token_auth_url'),
]
