from rest_framework import permissions

from api.utils import is_admin_user


class CategoryPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if is_admin_user(user):
            return True
        if request.method in permissions.SAFE_METHODS:
            return True

        return False


class GenrePermissions(CategoryPermissions):
    pass


class TitlePermissions(CategoryPermissions):
    pass
