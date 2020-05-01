from rest_framework import serializers

from ..models import Participation


class ParticipationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    url = serializers.HyperlinkedIdentityField("participation-detail", read_only=True)

    class Meta:
        model = Participation
        fields = (
            "url",
            "user",
            "event",
        )
        read_only_fields = ("url",)
