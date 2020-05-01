from django.contrib.auth.models import User
from django.db import models, transaction

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
        # Allows standardization of `IsOwnerOrReadOnly` permission
        # across models
        return self.user

    @transaction.atomic
    def save(self, *args, **kwargs):
        creation = not self.id
        if creation:
            self._increment_event_participants()
        super().save(*args, **kwargs)

    def _increment_event_participants(self):
        Event.objects.filter(id=self.event.id).update(
            num_participants=models.F("num_participants") + 1
        )

    @transaction.atomic
    def delete(self, *args, **kwargs):
        self._decrement_event_participants()
        super().delete(*args, **kwargs)

    def _decrement_event_participants(self):
        Event.objects.filter(id=self.event.id).update(
            num_participants=models.F("num_participants") - 1
        )

    class Meta:
        unique_together = ["user", "event"]
