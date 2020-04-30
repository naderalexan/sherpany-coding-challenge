from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema

from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from ..serializers import UserSerializer, ParticipationSerializer

tags = ["Participation"]


@method_decorator(
    name="create",
    decorator=swagger_auto_schema(
        tags=tags,
        operation_summary="Create Participation",
        operation_description="",
        responses={200: UserSerializer()},
    ),
)
class ParticipationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    permission_classes = (IsAuthenticated,)
    serializer_class = ParticipationSerializer
