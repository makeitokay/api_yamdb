from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, GenreViewSet, TitleViewSet


router_v1_api = DefaultRouter()
router_v1_api.register('categories', CategoryViewSet, basename='categories')
router_v1_api.register('genres', GenreViewSet, basename='genres')
router_v1_api.register('titles', TitleViewSet, basename='titles')

urlpatterns = [
    path('v1/', include(router_v1_api.urls)),
    path('v1/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]