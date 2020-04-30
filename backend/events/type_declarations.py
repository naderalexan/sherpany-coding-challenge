# flake8: noqa
"""
Custom types exporter.

Uses class Exporter to export identifier on code run to avoid circular imports
"""
import typing as t
import sys



class Exporter:
    """https://mail.python.org/pipermail/python-ideas/2012-May/014969.html"""

    def __getattr__(self, item: str) -> str:
        return item

    @classmethod
    def export_anything(cls, module_name: str) -> None:
        sys.modules[module_name] = cls()


if not t.TYPE_CHECKING:
    Exporter.export_anything(__name__)
else:
    """import custom classes here"""
    from django.contrib.auth.models import User
    from rest_framework.response import Response
    from rest_framework.request import Request
    from .serializers import UserSerializer
    from django.db.models.query import QuerySet
