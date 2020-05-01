from django.test import TestCase

from .mixins import TestsMixin

from ..factories import EventFactory, ParticipationFactory
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

        event.refresh_from_db()
        self.assertEqual(event.num_participants, 1)

    def test_create_unauthorized(self):
        event = EventFactory()

        payload = {"event": event.id}
        self.post(self.participation_list_url, data=payload, status_code=403)

    def test_delete(self):
        participation = ParticipationFactory(user=self.user)
        event = participation.event

        self.login()

        url = f"{self.participation_list_url}{participation.id}/"
        self.delete(url, status_code=204)
        self.assertFalse(Participation.objects.filter(id=participation.id).exists())

        event.refresh_from_db()
        self.assertEqual(event.num_participants, 0)

    def test_delete_unauthorized(self):
        participation = ParticipationFactory()

        url = f"{self.participation_list_url}{participation.id}/"
        self.delete(url, status_code=403)
        self.assertTrue(Participation.objects.filter(id=participation.id).exists())

        self.login()
        self.delete(url, status_code=404)
        self.assertTrue(Participation.objects.filter(id=participation.id).exists())
