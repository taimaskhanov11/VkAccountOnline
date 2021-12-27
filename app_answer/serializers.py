from rest_framework import serializers

from app_answer.models import Category, Input, Output


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
