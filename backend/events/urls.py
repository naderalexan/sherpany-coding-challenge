from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter

from . import views

schema_view = get_schema_view(
    openapi.Info(
        title="events API",
        default_version="v1",
        description="events API",
        terms_of_service="https://en.wikipedia.org/wiki/MIT_License#License_terms",
        contact=openapi.Contact(email="alexan.nader@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r"users", views.UserViewSet, basename="user")

urlpatterns = [
    path("", views.api_root, name="root"),
    path("auth/login/", views.LoginView.as_view(), name="login"),
    path("docs", schema_view.with_ui(cache_timeout=0),),
] + router.urls
