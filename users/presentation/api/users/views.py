from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import CreateUserSerializer, UserMeSerializer
from users.application.use_cases.create_user import CreateUserUseCase
from users.application.use_cases.get_user import GetUserUseCase
from users.domain.exceptions.user_exception import InvalidUserException
from users.domain.exceptions.user_exception import UserNotFoundException
from users.infraestructure.persistence.django.user_repository import DjangoUserRepository

from users.domain.entities.users import User


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


class UserMeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        use_case = GetUserUseCase(user_repository=DjangoUserRepository())

        try:
            user = use_case.execute(user_id=request.user.id)
            data = UserMeSerializer(
                {"id": user.id, "name": user.name, "email": user.email}
            ).data
            return Response(data, status=status.HTTP_200_OK)
        except UserNotFoundException as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
