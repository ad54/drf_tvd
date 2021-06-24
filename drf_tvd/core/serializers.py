from rest_framework import serializers
from .models import *
import re
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        # fields = "__all__"

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class BookSerializers(serializers.ModelSerializer):
    author = AuthorSerializers()
    class Meta:
        model = Book
        fields = "__all__"

    def validate(self, data):
        if not re.match('[A-Z]\-.\d*$',data['book_num']):
            raise serializers.ValidationError({'error': 'Please enter valid book number'})

        return data




