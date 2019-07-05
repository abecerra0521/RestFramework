from django.contrib.auth.models import Group, User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from sqlparse.engine.grouping import group


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('pk', 'url', 'first_name', 'last_name', 'username', 'email',
                  'is_staff', 'password')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        group = Group.objects.get(name="Users")
        group.user_set.add(user)
        return user