from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from users.serializers import YamdbTokenObtainSerializer


User = get_user_model()

class YamdbTokenObtainView(TokenObtainPairView):
    serializer_class = YamdbTokenObtainSerializer


class AuthView(APIView):
    http_method_names = ('post', )

    def post(self, request):
        user = get_object_or_404(User, email=request.data.get('email', None))    
        confirmation_code = User.objects.make_random_password()
        send_mail(
            "Confirmation Code",
            f'Confirmation code is {confirmation_code}',
            'test@test.mail',
            (user.email, ),
            fail_silently=False
        )
        user.confirmation_code = make_password(confirmation_code)
        user.save()
                
        return Response(status=status.HTTP_200_OK)