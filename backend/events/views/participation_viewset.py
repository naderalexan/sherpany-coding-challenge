from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema

from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from ..serializers import UserSerializer, ParticipationSerializer
from ..permissions import IsOwner

from .. import type_declarations as td

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
class ParticipationViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    # `IsOwner` permission is not really needed here, since the queryset filters
    # over logged in user, that being said, it has three uses:
    # 1. Explicit permissions
    # 2. Security measure if `get_queryset`
    # 3. Prettier than adding comments in `get_queryset`
    permission_classes = (IsAuthenticated, IsOwner, )
    serializer_class = ParticipationSerializer

    def get_queryset(self) -> td.QuerySet:
        return self.request.user.participations.all()
