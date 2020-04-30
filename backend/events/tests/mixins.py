import json

from django.urls import reverse

from ..factories import UserFactory, DUMMY_USER_PASSWORD


class TestsMixin(object):
    """
    base for API tests:
        * easy request calls, f.e.: self.post(url, data), self.get(url)
        * easy status check, f.e.: self.post(url, data, status_code=200)

    Source: https://github.com/Tivix/django-rest-auth/blob/
    624ad01afbc86fa15b4e652406f3bdcd01f36e00/rest_auth/tests/mixins.py#L32-L77
    """

    def send_request(self, request_method, *args, **kwargs):
        request_func = getattr(self.client, request_method)
        status_code = None
        if "content_type" not in kwargs and request_method != "get":
            kwargs["content_type"] = "application/json"
        if (
            "data" in kwargs
            and request_method != "get"
            and kwargs["content_type"] == "application/json"
        ):
            data = kwargs.get("data", "")
            kwargs["data"] = json.dumps(data)  # , cls=CustomJSONEncoder
        if "status_code" in kwargs:
            status_code = kwargs.pop("status_code")

        response = request_func(*args, **kwargs)
        if status_code:
            self.assertEqual(response.status_code, status_code)

        return response

    def post(self, *args, **kwargs):
        return self.send_request("post", *args, **kwargs)

    def get(self, *args, **kwargs):
        return self.send_request("get", *args, **kwargs)

    def patch(self, *args, **kwargs):
        return self.send_request("patch", *args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.send_request("delete", *args, **kwargs)

    def init(self):
        """Use in test by running `self.init()` in `setUp()`"""

        # Set up urls
        self.login_url = reverse("login")
        self.root_url = reverse("root")
        self.user_list_url = reverse("user-list")

        email = "foo@bar.com"
        self.user = UserFactory(email=email, username=email)
        self.password = DUMMY_USER_PASSWORD
