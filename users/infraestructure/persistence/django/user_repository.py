from domain.entities.users import User
from domain.ports.user_repository import UserRepository
from .models import UserModel


class DjangoUserRepository(UserRepository):
    def create(self, user: User) -> User:
        user_model = UserModel.objects.create(
            name=user.name, email=user.email, password=user.password
        )
        return self._to_domain(user_model)

    def get_by_id(self, user_id: int) -> User | None:
        try:
            user_model = UserModel.objects.get(id=user_id)
            return self._to_domain(user_model)
        except UserModel.DoesNotExist:
            return None

    def get_by_email(self, email: str) -> User | None:
        try:
            user_model = UserModel.objects.get(email=email)
            return self._to_domain(user_model)
        except UserModel.DoesNotExist:
            return None

    def update(self, user: User) -> User | None:
        try:
            user_model = UserModel.objects.get(id=user.id)
            user_model.name = user.name
            user_model.email = user.email
            user_model.password = user.password
            user_model.save()
            return self._to_domain(user_model)
        except UserModel.DoesNotExist:
            return None

    def delete(self, user_id: int) -> None:
        try:
            user_model = UserModel.objects.get(id=user_id)
            user_model.delete()
        except UserModel.DoesNotExist:
            pass

    def _to_domain(self, user_model: UserModel) -> User:
        return User(
            id=user_model.id,
            name=user_model.name,
            email=user_model.email,
            password=user_model.password,
        )
