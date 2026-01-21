from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from courses.presentation.api.courses.serializers import CourseSerializer
from courses.domain.entities.course import Course
from courses.application.use_cases.create_course import CreateCourseUseCase
from courses.infraestructure.persistence.django.course_repository import CourseRepositoryDjango
from rest_framework.permissions import IsAuthenticated

class CourseCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        course = Course(
            id=None,
            name=serializer.validated_data["name"],
            code=serializer.validated_data["code"],
            id_cine_field_detailed=serializer.validated_data["id_cine_field_detailed"],
            is_extension=serializer.validated_data["is_extension"],
            is_active=serializer.validated_data["is_active"],
        )
        created_course = use_case.execute(course)
        return Response({"id": created_course.id, "message": "Course created successfully"}, status=status.HTTP_201_CREATED)

