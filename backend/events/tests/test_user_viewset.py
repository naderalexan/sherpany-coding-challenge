from django.contrib.auth.models import User
from django.test import TestCase

from .mixins import TestsMixin


class UserViewSetTests(TestsMixin, TestCase):
    def setUp(self):
        self.init()

    def test_create(self):
        email = "hello@world.com"
        payload = {"email": email, "password": self.password}
        self.post(self.user_list_url, data=payload, status_code=201)
        self.assertTrue(user := User.objects.get(email=email))
        self.assertTrue(user.check_password(self.password))

    def test_create_invalid(self):
        email = "hello@world.com"
        payload = {"email": email}
        self.post(self.user_list_url, data=payload, status_code=400)
        self.assertFalse(User.objects.filter(email=email).exists())
