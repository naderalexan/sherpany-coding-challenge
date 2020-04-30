from django.test import TestCase

from .mixins import TestsMixin


class LoginTests(TestsMixin, TestCase):
    def setUp(self):
        self.init()

    def test_login(self):
        payload = {"email": self.user.email, "password": self.password}
        self.post(self.login_url, data=payload, status_code=200)
        self.assertEqual(
            int(self.client.session["_auth_user_id"]), self.user.id
        )

    def test_login_invalid(self):
        payload = {
            "email": self.user.email,
            "password": f"wrong {self.password}",
        }
        self.post(self.login_url, data=payload, status_code=400)
        self.assertFalse(self.client.session.get("_auth_user_id", False))

    def test_login_unregistered(self):
        payload = {"email": "unregistered@email.com", "password": "foobar"}
        self.post(self.login_url, data=payload, status_code=400)
        self.assertFalse(self.client.session.get("_auth_user_id", False))
