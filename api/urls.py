from django.urls import include, path

from rest_framework.routers import DefaultRouter

from api.users import views as users_views
from api.objects import views as objects_views
from api.activity import views as activity_views

router_v1_api = DefaultRouter()
router_v1_api.register(
    "categories", objects_views.CategoryViewSet, basename="categories"
)
router_v1_api.register("genres", objects_views.GenreViewSet, basename="genres")
router_v1_api.register("titles", objects_views.TitleViewSet, basename="titles")
router_v1_api.register("users", users_views.UserViewSet, basename="users")
router_v1_api.register(
    "titles/(?P<title_id>\d+)/reviews", activity_views.ReviewViewSet, basename="reviews"
)
router_v1_api.register(
    "titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments",
    activity_views.CommentViewSet,
    basename="comments",
)

urlpatterns = [
    path("v1/users/me/", users_views.UserSelfView.as_view()),
    path("v1/", include(router_v1_api.urls)),
    path("v1/auth/email/", users_views.AuthView.as_view()),
    path("v1/auth/token/", users_views.YamdbTokenObtainView.as_view()),
]
