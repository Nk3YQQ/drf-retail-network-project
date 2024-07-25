from django.urls import path

from users.apps import UsersConfig
from users.views import TokenObtainPairView, TokenRefreshView, UserProfileAPIView, UserRegistrationAPIView

app_name = UsersConfig.name

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("registration/", UserRegistrationAPIView.as_view(), name="registration"),
    path("profile/", UserProfileAPIView.as_view(), name="user_profile"),
]
