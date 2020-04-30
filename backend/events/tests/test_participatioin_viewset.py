from django.test import TestCase

from .mixins import TestsMixin

from ..factories import EventFactory
from ..models import Participation


class ParticipationViewSetTests(TestsMixin, TestCase):
    def setUp(self):
        self.init()

    def test_create(self):
        event = EventFactory()

        self.login()

        payload = {"event": event.id}
        self.post(self.participation_list_url, data=payload, status_code=201)
        self.assertTrue(
            Participation.objects.filter(event=event, user=self.user).exists()
        )

    def test_create_unauthorized(self):
        event = EventFactory()

        payload = {"event": event.id}
        self.post(self.participation_list_url, data=payload, status_code=403)
