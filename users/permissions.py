from rest_framework import permissions


class IsActiveUser(permissions.BasePermission):
    """Разрешение для доступа только активным пользователям."""

    def has_permission(self, request, view):
        return request.user.is_active
