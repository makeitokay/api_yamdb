from hashlib import sha256

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

User = get_user_model()

class YamdbAuthBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        email = kwargs['email']
        confirmation_code = request.data['confirmation_code']
        confirmation_code = sha256(confirmation_code.encode()).hexdigest()
        try:
            user = User.objects.get(email=email, confirmation_code=confirmation_code)
            return user
        except Exception: 
            pass

