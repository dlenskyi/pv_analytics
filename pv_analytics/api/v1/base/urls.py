from django.urls import path
from rest_framework import routers
from .api import (
    AuthApiView,
    LogoutApiView,
    CustomPasswordChangeView,
    UserApiView,
)


router = routers.DefaultRouter()

# Routes for CRUD operations under project apps
# ...

urlpatterns = [
    path(
        "auth/",
        AuthApiView.as_view(),
        name="auth",
    ),
    path(
        "logout/",
        LogoutApiView.as_view(),
        name="logout",
    ),
    path(
        "password/change/",
        CustomPasswordChangeView.as_view(),
        name="password-change",
    ),
    path(
        "user/",
        UserApiView.as_view(),
        name="user",
    ),
] + router.urls  # adding routes to urls
