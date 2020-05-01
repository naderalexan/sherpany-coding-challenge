import factory
from django.test import TestCase

from .mixins import TestsMixin

from ..factories import EventFactory
from ..models import Event


class EventViewSetTests(TestsMixin, TestCase):
    def setUp(self):
        self.init()

        self.event_dict = factory.build(dict, FACTORY_CLASS=EventFactory,)
        self.event_dict.pop("owner")

    def test_create(self):
        self.login()

        self.post(self.event_list_url, data=self.event_dict, status_code=201)
        self.assertTrue(Event.objects.filter(**self.event_dict).exists())

    def test_create_unauthorized(self):
        self.post(self.event_list_url, data=self.event_dict, status_code=403)

    def test_update_event(self):
        event = EventFactory(owner=self.user)

        self.login()

        url = f"{self.event_list_url}{event.id}/"
        self.patch(url, data=self.event_dict, status_code=200)
        self.assertTrue(Event.objects.filter(id=event.id, **self.event_dict).exists())

    def test_update_event_unauthorized(self):
        # creates a new user as owner for event
        event = EventFactory()

        self.login()

        url = f"{self.event_list_url}{event.id}/"
        self.patch(url, data=self.event_dict, status_code=403)
        self.assertFalse(Event.objects.filter(id=event.id, **self.event_dict).exists())

    def test_list(self):
        events = EventFactory.create_batch(5)
        res = self.get(self.event_list_url, status_code=200)
        self.assertEqual(len(events), len(res.data))
