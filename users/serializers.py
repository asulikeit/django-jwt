'''
Created on 2018. 10. 23.

@author: asulikeit
'''
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
 
    date = serializers.ReadOnlyField()
 
    class Meta(object):
        model = User
        fields = ('id', 'username', 'email', 'date')
        extra_kwargs = {'password': {'write_only': True}}