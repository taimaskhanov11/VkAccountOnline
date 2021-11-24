from django.contrib.auth import models
from rest_framework import serializers
from .models import Account, User, Category, Input, Output, Message, Numbers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


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


class MessageSerializer(serializers.HyperlinkedModelSerializer):
# class MessageSerializer(serializers.ModelSerializer,):
    class Meta:
        model = Message
        fields = '__all__'


class NumbersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Numbers
        fields = '__all__'
