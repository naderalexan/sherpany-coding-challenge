from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core import exceptions
from rest_framework import serializers

from .. import type_declarations as td


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(style={"input_type": "password"})

    def authenticate(self, **kwargs) -> td.User:
        return authenticate(self.context["request"], **kwargs)

    def validate(self, attrs: dict) -> dict:
        email = attrs.get("email")
        password = attrs.get("password")

        invalid_login_error_message = "Unable to log in with provided credentials."
        try:
            username = User.objects.get(email__iexact=email).get_username()
        except User.DoesNotExist:
            raise exceptions.ValidationError(invalid_login_error_message)

        user = self.authenticate(username=username, password=password)
        if user:
            if not user.is_active:
                error_msg = "User account is disabled."
                raise exceptions.ValidationError(error_msg)
        else:
            raise exceptions.ValidationError(invalid_login_error_message)
        attrs["user"] = user
        return attrs
