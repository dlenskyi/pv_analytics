from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import (
    gettext as _,
    gettext_lazy,
)

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=False,
        min_length=settings.ACCOUNT_USERNAME_MIN_LENGTH,
        max_length=settings.ACCOUNT_USERNAME_MAX_LENGTH,
    )
    email = serializers.EmailField(required=False)

    def validate_email(self, email):
        UserModel = get_user_model()

        exist_users = UserModel.objects.filter(email__iexact=email)
        if not exist_users:
            return email
        # Check if user owner of the email
        elif exist_users.count() == 1:
            if self.user() == exist_users.first():
                return email
            else:
                raise serializers.ValidationError(_('Email вже існує'))
        else:
            raise serializers.ValidationError(_('Email вже існує'))

    def user(self):
        request = self.context.get("request")
        if request and hasattr(request, 'user'):
            return request.user
        return None

    def validate_username(self, username):
        UserModel = get_user_model()
        exist_users = UserModel.objects.filter(username__iexact=username)
        if not exist_users:
            return username
        # Check if user owner of the username
        elif exist_users.count() == 1:
            if self.user() == exist_users.first():
                return username
            else:
                raise serializers.ValidationError(_('Логін вже існує'))
        else:
            raise serializers.ValidationError(_('Логін вже існує'))

    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'username',
        )
