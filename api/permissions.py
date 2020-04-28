from rest_framework import permissions


class IsAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            obj == request.user
            or request.user.role == "admin"
            or request.user.is_superuser
        )


class IsAdminOrModeratorOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.role == "admin" or request.user.is_superuser
