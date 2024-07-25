from rest_framework.permissions import BasePermission


class IsActiveUser(BasePermission):
    """Ограничение для неактивных пользователей"""

    def has_permission(self, request, view):
        return request.user and request.user.is_active
