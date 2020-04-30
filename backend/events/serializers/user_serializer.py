from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email",)


class UserCreateSerializer(UserSerializer):
    def create(self, validated_data):
        validated_data["username"] = validated_data["email"]
        return User.objects.create_user(**validated_data)

    class Meta(UserSerializer.Meta):
        model = User
        fields = UserSerializer.Meta.fields + ("password",)
