from django.contrib.auth import authenticate

from rest_framework.serializers import CharField
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class YamdbTokenObtainSerializer(TokenObtainSerializer):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        del self.fields['password']
        self.fields['confirmation_code'] = CharField()

    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        authenticate_kwargs = {
            self.username_field: attrs[self.username_field],
            'confirmation_code': attrs['confirmation_code'],
        }
        try:
            authenticate_kwargs['request'] = self.context['request']
        except KeyError:
            pass
        user = authenticate(**authenticate_kwargs)

        if user is None:
            return self.default_error_messages

        refresh = self.get_token(user)

        data = dict({
            'token': str(refresh.access_token)
        })

        return data

        