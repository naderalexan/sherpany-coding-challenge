from django.test import TestCase

from .mixins import TestsMixin


class ApiRootTests(TestsMixin, TestCase):
    def setUp(self):
        self.init()

    def test_get(self):
        self.get(self.root_url, status_code=200)
