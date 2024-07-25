from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView as BaseTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView as BaseTokenRefreshView

from users.models import User
from users.permissions import IsActiveUser
from users.serializers import UserRegistrationSerializer, UserSerializer


@extend_schema_view(create=extend_schema(description="Create a new refresh token"))
class TokenRefreshView(BaseTokenRefreshView):
    """Контроллер для создания refresh токена"""

    pass


@extend_schema_view(create=extend_schema(description="Create a new access token"))
class TokenObtainPairView(BaseTokenObtainPairView):
    """Контроллер для создания access токена"""

    pass


class UserRegistrationAPIView(CreateAPIView):
    """Контроллер для регистрации пользователя"""

    serializer_class = UserRegistrationSerializer


class UserProfileAPIView(RetrieveAPIView):
    """Контроллер для профиля пользователя"""

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]

    def get_object(self):
        pk = self.request.user.pk

        return User.objects.get(pk=pk)
