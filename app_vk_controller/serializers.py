from django.contrib.auth import models
from rest_framework import serializers
from .models import Account, User, Category, Input, Output, Message, Number


# class UserSerializer(serializers.HyperlinkedModelSerializer):
class UserSerializer(serializers.ModelSerializer, ):
    class Meta:
        model = User
        fields = '__all__'


# class AccountSerializer(serializers.HyperlinkedModelSerializer):
class AccountSerializer(serializers.ModelSerializer, ):
    class Meta:
        model = Account
        fields = '__all__'
        # fields = ['id', 'first_name', 'last_name']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class InputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Input
        fields = '__all__'


class OutputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Output
        fields = '__all__'


# class MessageSerializer(serializers.HyperlinkedModelSerializer):
class MessageSerializer(serializers.ModelSerializer, ):
    account = AccountSerializer()
    user = UserSerializer()

    class Meta:
        model = Message
        fields = '__all__'


class NumberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Number
        fields = '__all__'
