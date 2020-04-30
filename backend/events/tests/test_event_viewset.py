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
