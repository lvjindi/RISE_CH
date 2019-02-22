# -*-coding:utf-8 -*-
from rest_framework import serializers


class SliderSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    flag = serializers.ChoiceField(choices=(0, 1, 2))
    articleId = serializers.CharField(max_length=4)
    image = serializers.CharField(max_length=64)
    imagePath=serializers.CharField(max_length=64)
    create_time = serializers.DateTimeField()


class CreateSliderSerializer(serializers.Serializer):
    flag = serializers.ChoiceField(choices=(0, 1, 2))
    articleId = serializers.IntegerField()
    image = serializers.CharField(max_length=64)


class EditSliderSerializer(serializers.Serializer):
    flag = serializers.ChoiceField(choices=(0, 1, 2))
    articleId = serializers.IntegerField()
    image = serializers.CharField(max_length=64)


class MessageFromDrSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    content = serializers.CharField(max_length=1024 * 1024 * 8)
    title = serializers.CharField(max_length=64)
    image = serializers.CharField(max_length=64)
    imagePath = serializers.CharField(max_length=64)
    create_time = serializers.DateTimeField()


class CreateMessageSerializer(serializers.Serializer):
    content = serializers.CharField(max_length=1024 * 1024 * 8)
    title = serializers.CharField(max_length=64)
    image = serializers.CharField(max_length=64)
