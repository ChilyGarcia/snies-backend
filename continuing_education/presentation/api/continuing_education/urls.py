from django.urls import path
from continuing_education.presentation.api.continuing_education.views import ContinuingEducationCreateAPIView

urlpatterns = [
    path('create/', ContinuingEducationCreateAPIView.as_view(), name='continuing_education-create'),
]
