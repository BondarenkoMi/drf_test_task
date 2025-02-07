from django.urls import path

from .views import UserCreateAPIView, UserDetailAPIView

urlpatterns = [
    path('<int:pk>/', UserDetailAPIView.as_view(), name='user_detail'),
    path('', UserCreateAPIView.as_view(), name='user_create'),
]
