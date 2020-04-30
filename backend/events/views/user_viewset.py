from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from drf_yasg.utils import swagger_auto_schema

from rest_framework import viewsets, mixins, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from ..serializers import UserSerializer, UserCreateSerializer

from .. import type_declarations as td

sensitive_post_parameters_m = method_decorator(sensitive_post_parameters("password",))
tags = ["Users"]


@method_decorator(
    name="create",
    decorator=swagger_auto_schema(
        tags=tags,
        operation_summary="Create User",
        operation_description="",
        responses={200: UserSerializer()},
    ),
)
class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    permission_classes = (AllowAny,)
    serializer_class = UserCreateSerializer

    def create(self, request: td.Request, *args, **kwargs) -> td.Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        instance = serializer.instance
        response_serializer = UserSerializer(instance=instance)
        headers = self.get_success_headers(serializer.data)
        return Response(
            response_serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
