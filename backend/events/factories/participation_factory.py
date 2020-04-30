import factory

from .user_factory import UserFactory
from .event_factory import EventFactory
from ..models import Participation


class ParticipationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Participation

    user = factory.SubFactory(UserFactory)
    event = factory.SubFactory(EventFactory)
