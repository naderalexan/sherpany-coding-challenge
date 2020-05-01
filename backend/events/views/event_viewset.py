from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from ..models import Event
from ..serializers import EventSerializer
from ..permissions import IsOwner


class EventViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet
):
    permission_classes = (IsAuthenticated, IsOwner)
    serializer_class = EventSerializer
    queryset = Event.objects.all()
