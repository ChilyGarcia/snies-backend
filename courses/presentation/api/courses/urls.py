from django.urls import path
from .views import CourseCreateAPIView

urlpatterns = [
    path("create/", CourseCreateAPIView.as_view()),
]
