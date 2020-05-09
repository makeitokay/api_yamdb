from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

from rest_framework_simplejwt.serializers import PasswordField, RefreshToken


class YamdbTokenObtainSerializer(serializers.Serializer):

    default_error_messages = {
        'no_active_account': _('No active account found with the given credentials')
    }
    
    def __init__(self, *args, **kwargs):           
        super().__init__(*args, **kwargs)

        self.fields['email'] = serializers.CharField()
        self.fields['confirmation_code'] = PasswordField()

    def validate(self, attrs):
        authenticate_kwargs = {
            'email': attrs['email'],
            'confirmation_code': attrs['confirmation_code'],
        }
        try:
            authenticate_kwargs['request'] = self.context['request']
        except KeyError:
            pass

        user = authenticate(**authenticate_kwargs)

        if user is None:
            return self.default_error_messages
        
        refresh = RefreshToken.for_user(user)
        token = refresh.access_token

        data = dict({
            'token': str(token)
        })

        return data

        