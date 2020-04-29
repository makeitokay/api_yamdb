from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
 )

from auth import views as auth_views
from api import views

router = DefaultRouter()
router.register('users', views.UserViewSet, basename='User')

urlpatterns = [    
    path('v1/', include(router.urls)),
    path('v1/auth/email/', auth_views.AuthView.as_view(), ),
    path('v1/auth/token/', auth_views.YamdbTokenObtainView.as_view(), ),
    path('v1/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]