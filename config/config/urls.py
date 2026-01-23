from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("users.presentation.api.auth.urls")),
    path("api/users/", include("users.presentation.api.users.urls")),
    path("api/roles/", include("users.presentation.api.roles.urls")),
    path("api/courses/", include("courses.presentation.api.courses.urls")),
    path(
        "api/continuing_education/",
        include("continuing_education.presentation.api.continuing_education.urls"),
    ),
    path(
        "api/wellbeing_activities/",
        include("wellbeing_activities.presentation.api.wellbeing_activities.urls"),
    ),
    path(
        "api/wellbeing_beneficiaries/",
        include("wellbeing_beneficiaries.presentation.api.wellbeing_beneficiaries.urls"),
    ),
]
