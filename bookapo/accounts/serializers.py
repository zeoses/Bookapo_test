from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'is_active', 'last_login']


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    def validate(self, attrs):
        return super().validate(attrs)

    class Meta:
        model = Profile
        fields = ['pk', 'user', 'last_activity_time']
