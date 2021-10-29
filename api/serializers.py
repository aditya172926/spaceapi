from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserData

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'date_joined'
        ]

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'password'
        ]
        extra_kwargs = { 'password': {'write_only': True, 'required': True}}
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = [
            'author',
            'origin',
            'continent',
            'country'
        ]