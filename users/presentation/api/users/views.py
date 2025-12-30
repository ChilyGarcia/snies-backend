from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CreateUserSerializer
from application.use_cases.create_user import CreateUserUseCase
from domain.exceptions.user_exception import InvalidUserException
from infraestructure.persistence.django.user_repository import DjangoUserRepository

from domain.entities.users import User


class UserCreateAPIView(APIView):
    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        use_case = CreateUserUseCase(user_repository=DjangoUserRepository())

        try:
            user = User(
                id=None,
                name=serializer.validated_data["name"],
                email=serializer.validated_data["email"],
                password=serializer.validated_data["password"],
            )
            created_user = use_case.execute(user)
            return Response({"id": created_user.id}, status=status.HTTP_201_CREATED)
        except InvalidUserException as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
