from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.response import Response

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','first_name','last_name', 'username', 'email', 'is_staff')


    def retrievebyuser(self, request, username=None):
        """GET - Show <email> user"""
        api_result = User.objects.filter(username=username).first() 
        return Response(api_result)