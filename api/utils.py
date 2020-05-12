def is_admin_user(user):
    if not user.is_authenticated:
        return False
    return user.role == "admin" or user.is_superuser
