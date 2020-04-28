from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ReviewViewSet, CommentViewSet

router_v1_api = DefaultRouter()
router_v1_api.register('titles/(?P<title_id>\d+)/reviews', ReviewViewSet)
router_v1_api.register('titles/(?P<title_id>\d+)/comments', CommentViewSet)

urlpatterns = [
    path('', include(router_v1_api.urls)),
]
