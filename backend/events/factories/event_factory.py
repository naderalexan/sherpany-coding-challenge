import factory

from .user_factory import UserFactory
from ..models import Event


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event

    owner = factory.SubFactory(UserFactory)

    title = factory.Sequence(lambda n: f"Event {n}")
    description = factory.Faker("text")
    date = factory.Faker("date")
