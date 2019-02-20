# -*-coding:utf-8 -*-
from rest_framework import serializers

from people.models import People


class PeopleInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=10)
    office = serializers.CharField(max_length=128)
    phone = serializers.CharField(max_length=16)
    email = serializers.CharField(max_length=32)
    profession = serializers.CharField(max_length=32)
    position = serializers.CharField(max_length=32)
    degree = serializers.CharField(max_length=32)
    degreeId = serializers.IntegerField()
    professionalTitle = serializers.CharField(max_length=32)
    area = serializers.CharField(max_length=64)
    create_time = serializers.DateTimeField()


class PeopleDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    interesting = serializers.CharField(max_length=1024 * 1024 * 8)
    introduce = serializers.CharField(max_length=1024 * 1024 * 8)
    project = serializers.CharField(max_length=1024 * 1024 * 8)
    achievement = serializers.CharField(max_length=1024 * 1024 * 8)
    activity = serializers.CharField(max_length=1024 * 1024 * 8)
    papers = serializers.CharField(max_length=1024 * 1024 * 8)
    report = serializers.CharField(max_length=1024 * 1024 * 8)
    link = serializers.CharField(max_length=1024 * 1024 * 8)
    img = serializers.CharField(max_length=128)
    create_time = serializers.DateTimeField()


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        exclude = ["last_update_time"]


class CreatePeopleSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)
    office = serializers.CharField(max_length=128)
    phone = serializers.CharField(max_length=16)
    email = serializers.CharField(max_length=32)
    profession = serializers.CharField(max_length=32)
    position = serializers.CharField(max_length=32)
    degree = serializers.CharField(max_length=32)
    degreeId = serializers.IntegerField()
    professionalTitle = serializers.CharField(max_length=32)
    area = serializers.CharField(max_length=64)
    interesting = serializers.CharField(max_length=1024 * 1024 * 8)
    introduce = serializers.CharField(max_length=1024 * 1024 * 8)
    project = serializers.CharField(max_length=1024 * 1024 * 8)
    achievement = serializers.CharField(max_length=1024 * 1024 * 8)
    activity = serializers.CharField(max_length=1024 * 1024 * 8)
    papers = serializers.CharField(max_length=1024 * 1024 * 8)
    report = serializers.CharField(max_length=1024 * 1024 * 8)
    link = serializers.CharField(max_length=1024 * 1024 * 8)
    img = serializers.CharField(max_length=128)
