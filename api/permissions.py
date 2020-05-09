from rest_framework import permissions
    

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
            request.user.role == "admin"
            or request.user.is_superuser
            or (
                 obj == request.user 
                 and request.data.get('role') == 'user'
            )
        )
            

class DenyRoleChanging(permissions.BasePermission):
    def has_permission(self, request, view):
        role = request.data.get('role', None)
        return bool(
            role is None 
            or request.user.role == role
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
