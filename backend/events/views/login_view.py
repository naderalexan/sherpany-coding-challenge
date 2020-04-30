from django.contrib.auth import login as django_login
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from drf_yasg.utils import swagger_auto_schema

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny

from ..serializers import UserSerializer, LoginSerializer

from .. import type_declarations as td

sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters(
        "password",
    )
)
tags = ["Authentication"]


@method_decorator(
    name="post",
    decorator=swagger_auto_schema(
        tags=tags,
        operation_summary="Login",
        operation_description="",
        responses={200: UserSerializer()},
    ),
)
class LoginView(GenericAPIView):

    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs) -> td.Response:
        return super().dispatch(*args, **kwargs)

    def process_login(self) -> None:
        django_login(self.request, self.user)

    @staticmethod
    def get_response_serializer() -> td.UserSerializer:
        return UserSerializer

    def login(self) -> None:
        self.user = self.serializer.validated_data["user"]
        self.process_login()

    def get_response(self) -> td.Response:
        serializer_class = self.get_response_serializer()
        serializer = serializer_class(
            instance=self.user, context={"request": self.request}
        )
        response = Response(serializer.data, status=status.HTTP_200_OK)
        return response

    def post(self, request, *args, **kwargs) -> td.Response:
        self.request = request
        self.serializer = self.get_serializer(
            data=self.request.data, context={"request": request}
        )
        self.serializer.is_valid(raise_exception=True)

        self.login()
        return self.get_response()
