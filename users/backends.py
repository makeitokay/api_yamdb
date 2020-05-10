from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password

User = get_user_model()


class YamdbAuthBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        try:
            confirmation_code = request.data["confirmation_code"]
            user = User.objects.get(email=kwargs["email"])
            if check_password(confirmation_code, user.confirmation_code):
                return user
        except:
            pass
