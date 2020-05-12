from rest_framework import permissions

from api.utils import is_admin_user


class ReviewPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if is_admin_user(user):
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == "DELETE" and user.role == "moderator":
            return True

        return user == obj.author


class CommentPermissions(ReviewPermissions):
    pass
