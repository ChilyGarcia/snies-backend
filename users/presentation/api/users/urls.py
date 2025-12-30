from django.urls import path
from .views import UserCreateAPIView

urlpatterns = [
    path("users/", UserCreateAPIView.as_view()),
]
