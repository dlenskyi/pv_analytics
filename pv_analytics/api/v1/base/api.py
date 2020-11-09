from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.admin import sensitive_post_parameters_m
from rest_auth.serializers import PasswordChangeSerializer
from rest_framework import (
    viewsets,
    views,
    generics,
    status,
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.utils.translation import gettext as _
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN

from pv_analytics.apps.users.permissions import IsAuthenticated
from .serializers import UserSerializer


class AuthApiView(generics.GenericAPIView):
    permission_classes = [
        AllowAny,
    ]

    def post(self, request, *args, **kwargs):
        required_params = ['username', 'password']

        if not all(r_param in request.data for r_param in required_params):
            return Response(
                {'error': _('Будь ласка, надайте логін та пароль.')},
                status=HTTP_400_BAD_REQUEST,
            )

        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if not user:
            return Response(
                {'error': _('Невірні дані.')}, status=HTTP_400_BAD_REQUEST,
            )
        if not user.is_active:
            return Response(
                {'error': _('Акаунт заблоковано.')}, status=HTTP_403_FORBIDDEN
            )

        login(request, user)

        return Response(
            {'username': user.username, 'is_admin': user.is_superuser}
        )


class LogoutApiView(generics.GenericAPIView):
    permission_classes = [
        AllowAny,
    ]

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomPasswordChangeView(generics.GenericAPIView):
    """
        Calls Django Auth SetPasswordForm save method.

        Accepts the following POST parameters: new_password1, new_password2
        Returns the success/fail message.
    """

    serializer_class = PasswordChangeSerializer
    permission_classes = (IsAuthenticated,)

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(CustomPasswordChangeView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        old_pass = request.data.get('old_password')
        new_pass = request.data.get('new_password1')
        if old_pass == new_pass:
            return Response(
                {"error": _("Неможливо змінити пароль на такий же.")}
            )
        serializer.save()

        return Response({"detail": _("Новий пароль збережено.")})


class UserApiView(generics.GenericAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    def patch(self, request):
        serializer = self.get_serializer(
            instance=request.user,
            data=request.data,
            context={'request': request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data)
