from rest_framework import serializers

from ..models import Event


class EventSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Event
        fields = (
            "title",
            "description",
            "date",
            "owner",
        )
