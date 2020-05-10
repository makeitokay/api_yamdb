from rest_framework import permissions


def _is_admin_user(user):
    if not user.is_authenticated:
        return False
    return user.role == "admin" or user.is_superuser


class IsYamdbAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return _is_admin_user(request.user)


class DenyRoleChanging(permissions.BasePermission):
    def has_permission(self, request, view):
        role = request.data.get("role", None)
        return bool(role is None or request.user.role == role)


class ReviewPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if _is_admin_user(user):
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == "DELETE" and user.role == "moderator":
            return True

        return user == obj.author


class CommentPermissions(ReviewPermissions):
    pass


class CategoryPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if _is_admin_user(user):
            return True
        if request.method in permissions.SAFE_METHODS:
            return True

        return False


class GenrePermissions(CategoryPermissions):
    pass


class TitlePermissions(CategoryPermissions):
    pass
