from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from ..serializers import ParticipationSerializer
from ..permissions import IsOwner

from .. import type_declarations as td

tags = ["Participation"]


class ParticipationViewSet(
    mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet
):
    # `IsOwner` permission is not really needed here, since the queryset filters
    # over logged in user, that being said, it has three uses:
    # 1. Explicit permissions
    # 2. Security measure if `get_queryset` gets changed
    # 3. Prettier than adding comments in `get_queryset`
    permission_classes = (
        IsAuthenticated,
        IsOwner,
    )
    serializer_class = ParticipationSerializer

    def get_queryset(self) -> td.QuerySet:
        return self.request.user.participations.all()
