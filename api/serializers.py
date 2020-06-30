''' API Serializers'''
#REST FRAMEWORK
from rest_framework import serializers
#Django
from django.contrib.auth.models import User

class UserSerializers(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        user = User()
        user.first_name = validated_data.get('first_name')
        user.last_name = validated_data.get('last_name')
        user.username = validated_data.get('username')
        user.email = validated_data.get('email')
        user.set_password(validated_data.get('password'))
        user.save()
        return user

    def validate_user(self, data):
        user = User.objects.filter(username = data)
        if(user):
            raise serializers.ValidationError('This username is already taken')
        else:
            return data

