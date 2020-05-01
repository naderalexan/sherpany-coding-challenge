from django.contrib.auth.models import User
from django.db import models

from .event import Event


class Participation(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="participations"
    )
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="participations"
    )

    @property
    def owner(self):
        # Allows standardization of `IsOwner` permission
        # across models
        return self.user
