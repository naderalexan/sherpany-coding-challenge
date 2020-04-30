import factory
from django.contrib.auth.models import User


DUMMY_USER_PASSWORD = "super secret"


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    username = factory.Faker("user_name")
    email = factory.Faker("email")
    password = factory.PostGenerationMethodCall("set_password", DUMMY_USER_PASSWORD)
    is_active = True
