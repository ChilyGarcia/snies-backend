from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("users.presentation.api.auth.urls")),
    path("api/courses/", include("courses.presentation.api.courses.urls")),
    path(
        "api/continuing_education/",
        include("continuing_education.presentation.api.continuing_education.urls"),
    ),
]
