from rest_framework import serializers

from app_answer.models import Category, Input, Output


# class InputSerializer(serializers.HyperlinkedModelSerializer):
class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Input
        fields = '__all__'


# class OutputSerializer(serializers.HyperlinkedModelSerializer):
class OutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Output
        fields = '__all__'


# class CategorySerializer(serializers.HyperlinkedModelSerializer):
class CategorySerializer(serializers.ModelSerializer):
    inputs = InputSerializer(many=True)
    outputs = OutputSerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'
