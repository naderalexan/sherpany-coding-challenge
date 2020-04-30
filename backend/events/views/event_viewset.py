from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from ..serializers import EventSerializer


class EventViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = EventSerializer
