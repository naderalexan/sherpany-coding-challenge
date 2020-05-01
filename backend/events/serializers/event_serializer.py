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


class EventListSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()

    def get_owner(self, instance):
        email = instance.owner.email
        [handle, _] = email.split("@")
        return handle

    class Meta:
        model = Event
        fields = (
            "title",
            "date",
            "owner",
            "num_participants",
        )
