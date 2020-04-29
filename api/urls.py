from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from auth import views as auth_views
from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet, UserViewSet)

router_v1_api = DefaultRouter()
router_v1_api.register("categories", CategoryViewSet, basename="categories")
router_v1_api.register("genres", GenreViewSet, basename="genres")
router_v1_api.register("titles", TitleViewSet, basename="titles")
router_v1_api.register("users", UserViewSet, basename="users")
router_v1_api.register("titles/(?P<title_id>\d+)/reviews", ReviewViewSet, basename='reviews')
router_v1_api.register(
    "titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments",
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path("v1/", include(router_v1_api.urls)),
    path('v1/auth/email/', auth_views.AuthView.as_view(), ),
    path('v1/auth/token/', auth_views.YamdbTokenObtainView.as_view()), 
]
