from djoser.serializers import UserCreateSerializer
from account.models import CustomUser
from rest_framework import serializers



class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'lastname', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        
        


