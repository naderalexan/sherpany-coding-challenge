from rest_framework import serializers

from ..models import Participation


class ParticipationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Participation
        fields = (
            "user",
            "event",
        )
