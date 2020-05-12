from rest_framework import permissions

from api.utils import is_admin_user


class IsYamdbAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return is_admin_user(request.user)


class DenyRoleChanging(permissions.BasePermission):
    def has_permission(self, request, view):
        role = request.data.get("role", None)
        return bool(role is None or request.user.role == role)
