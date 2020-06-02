from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *

class UserSerializers(UserCreateSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'first_name', 'last_name', 'phone')