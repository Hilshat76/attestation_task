from django.contrib.auth.hashers import make_password
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        """Создаём нового пользователя и сразу хешируем пароль"""
        # Получаем данные из сериализатора
        user_data = serializer.validated_data

        # Хешируем пароль перед сохранением
        user_data["password"] = make_password(user_data["password"])  # Хешируем пароль
        user_data["is_active"] = (
            False  # Устанавливаем is_active false, чтобы админ мог активировать самостоятельно
        )

        # Сохраняем пользователя с хешированным паролем
        serializer.save(**user_data)
