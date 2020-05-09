from rest_framework import permissions


class IsAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            obj == request.user
            or request.user.role == "admin"
            or request.user.is_superuser
        )


class UserPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ('list', 'create', 'destroy'):
            return bool (
                request.user.role == 'admin'
                or request.user.is_superuser
            )
        
        return True
    
    def has_object_permission(self, request, view, obj):
        return bool (
                obj == request.user
                or request.user.role == 'admin'
                or request.user.is_superuser
            )


class ReviewPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if request.method in permissions.SAFE_METHODS or user.role == 'admin' or user.is_superuser:
            return True
        if request.method == 'DELETE' and user.role == 'moderator':
            return True

        return user == obj.author


class CommentPermissions(ReviewPermissions):
    pass
