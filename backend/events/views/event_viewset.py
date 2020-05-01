from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ..models import Event
from ..serializers import EventSerializer, EventListSerializer
from ..permissions import IsOwnerOrReadOnly


class EventViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    queryset = Event.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return EventListSerializer
        return EventSerializer
