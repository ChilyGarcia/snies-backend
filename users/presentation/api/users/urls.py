from django.urls import path
from .views import UserCreateAPIView, UserMeAPIView

urlpatterns = [
    path("", UserCreateAPIView.as_view()),
    path("me/", UserMeAPIView.as_view()),
]
