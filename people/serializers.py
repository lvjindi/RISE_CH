# -*-coding:utf-8 -*-
from rest_framework import serializers


class StaffInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    imgPath = serializers.CharField(max_length=128)
    name = serializers.CharField(max_length=10)
    status = serializers.ChoiceField(choices=['在职', '不在职'])
    office = serializers.CharField(max_length=128)
    phone = serializers.CharField(max_length=16)
    email = serializers.CharField(max_length=32)
    position = serializers.CharField(max_length=32)
    degree = serializers.CharField(max_length=32)
    professionalTitle = serializers.CharField(max_length=32)
    profession = serializers.ChoiceField(choices=['博士导师', '硕士导师'])
    area = serializers.CharField(max_length=64)
    link = serializers.CharField(max_length=256)
    create_time = serializers.DateTimeField()


class StaffDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    interesting = serializers.CharField(max_length=1024 * 1024 * 8)
    biography = serializers.CharField(max_length=1024 * 1024 * 8)
    project = serializers.CharField(max_length=1024 * 1024 * 8)
    achievement = serializers.CharField(max_length=1024 * 1024 * 8)
    activity = serializers.CharField(max_length=1024 * 1024 * 8)
    publication = serializers.CharField(max_length=1024 * 1024 * 8)
    report = serializers.CharField(max_length=1024 * 1024 * 8)
    create_time = serializers.DateTimeField()


class StaffSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=30)
    office = serializers.CharField(max_length=128)
    phone = serializers.CharField(max_length=16)
    email = serializers.CharField(max_length=32)
    position = serializers.CharField(max_length=32)
    degree = serializers.CharField(max_length=32)
    professionalTitle = serializers.CharField(max_length=32)
    profession = serializers.CharField(max_length=32)
    area = serializers.CharField(max_length=64)
    interesting = serializers.CharField(max_length=1024 * 1024 * 8)
    biography = serializers.CharField(max_length=1024 * 1024 * 8)
    project = serializers.CharField(max_length=1024 * 1024 * 8)
    achievement = serializers.CharField(max_length=1024 * 1024 * 8)
    activity = serializers.CharField(max_length=1024 * 1024 * 8)
    publication = serializers.CharField(max_length=1024 * 1024 * 8)
    report = serializers.CharField(max_length=1024 * 1024 * 8)
    img = serializers.CharField(max_length=128)
    imgPath = serializers.CharField(max_length=128)
    link = serializers.CharField(max_length=256)
    create_time = serializers.DateTimeField()


class StudentInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    imgPath = serializers.CharField(max_length=128)
    name = serializers.CharField(max_length=10)
    enrollmentTime = serializers.DateTimeField()
    graduationTime = serializers.DateTimeField()
    type = serializers.ChoiceField(choices=['硕士', '博士', '本科生'])
    graduateStatus = serializers.ChoiceField(choices=['在读', '毕业'])
    supervisor = serializers.ChoiceField(choices=['刘志明教授', '赖红副教授', '叶明副教授'])
    supervisorLink = serializers.CharField(max_length=256)
    email = serializers.CharField(max_length=32)
    area = serializers.CharField(max_length=64)
    link = serializers.CharField(max_length=256)
    create_time = serializers.DateTimeField()


class StudentDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    biography = serializers.CharField(max_length=1024 * 1024 * 8)
    project = serializers.CharField(max_length=1024 * 1024 * 8)
    activity = serializers.CharField(max_length=1024 * 1024 * 8)
    publication = serializers.CharField(max_length=1024 * 1024 * 8)
    create_time = serializers.DateTimeField()


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=30)
    email = serializers.CharField(max_length=32)
    enrollmentTime = serializers.DateTimeField()
    graduationTime = serializers.DateTimeField()
    type = serializers.ChoiceField(choices=['硕士', '博士', '本科生'])
    graduateStatus = serializers.ChoiceField(choices=['在读', '毕业'])
    supervisor = serializers.CharField(max_length=64)
    supervisorLink = serializers.CharField(max_length=256)
    area = serializers.CharField(max_length=64)
    img = serializers.CharField(max_length=128)
    imgPath = serializers.CharField(max_length=128)
    biography = serializers.CharField(max_length=1024 * 1024 * 8)
    project = serializers.CharField(max_length=1024 * 1024 * 8)
    activity = serializers.CharField(max_length=1024 * 1024 * 8)
    publication = serializers.CharField(max_length=1024 * 1024 * 8)
    link = serializers.CharField(max_length=256)
    create_time = serializers.DateTimeField()


class AdjunctProfessorInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    imgPath = serializers.CharField(max_length=128)
    name = serializers.CharField(max_length=10)
    email = serializers.CharField(max_length=32)
    degree = serializers.CharField(max_length=32)
    professionalTitle = serializers.CharField(max_length=32)
    area = serializers.CharField(max_length=64)
    link = serializers.CharField(max_length=256)
    create_time = serializers.DateTimeField()


class AdjunctProfessorDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    biography = serializers.CharField(max_length=1024 * 1024 * 8)
    create_time = serializers.DateTimeField()


class AdjunctProfessorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=30)
    email = serializers.CharField(max_length=32)
    degree = serializers.CharField(max_length=32)
    professionalTitle = serializers.CharField(max_length=32)
    img = serializers.CharField(max_length=128)
    imgPath = serializers.CharField(max_length=128)
    area = serializers.CharField(max_length=64)
    biography = serializers.CharField(max_length=1024 * 1024 * 8)
    link = serializers.CharField(max_length=256)
    create_time = serializers.DateTimeField()
