from rest_framework import serializers

from conference.models import ConferenceType


class ConferenceListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=128)
    type = serializers.ChoiceField(choices=[ConferenceType.Domestic, ConferenceType.Foreign])
    create_time = serializers.DateTimeField()


class ConferenceDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    content = serializers.CharField(max_length=1024 * 1024 * 8)
    type = serializers.ChoiceField(choices=[ConferenceType.Domestic, ConferenceType.Foreign])
    views_number = serializers.IntegerField()
    image = serializers.CharField(max_length=128)
    sliderFlag = serializers.BooleanField()


class CreateConferenceSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=128)
    content = serializers.CharField(max_length=1024 * 1024 * 8)
    type = serializers.ChoiceField(choices=[ConferenceType.Domestic, ConferenceType.Foreign])
    image = serializers.CharField(max_length=128)
    sliderFlag = serializers.BooleanField()


class ConferenceSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=128)
    content = serializers.CharField(max_length=1024 * 1024 * 8)
    type = serializers.ChoiceField(choices=[ConferenceType.Domestic, ConferenceType.Foreign])
    views_number = serializers.IntegerField()
    image = serializers.CharField(max_length=128)
    sliderFlag = serializers.BooleanField()
    create_time = serializers.DateTimeField()
