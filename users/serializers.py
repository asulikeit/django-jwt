from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
 
    date = serializers.ReadOnlyField()
    password = serializers.CharField(min_length=8, write_only=True)
 
    class Meta(object):
        model = User
        fields = ('id', 'username', 'email', 'date', 'password')
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)