from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "login": reverse("login", request=request, format=format),
            "participations": reverse(
                "participation-list", request=request, format=format
            ),
            "users": reverse("user-list", request=request, format=format),
        }
    )
