from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name="events")
    title = models.CharField(max_length=64)
    description = models.TextField()
    date = models.DateField()
    num_participants = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ("-date",)
