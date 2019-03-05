from rest_framework import serializers

from conference.models import Conference


class ConferenceListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=128)
    type = serializers.ChoiceField(choices=Conference.ConferenceType)
    create_time = serializers.DateTimeField()


class ConferenceDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=128)
    news_id = serializers.IntegerField()
    content = serializers.CharField(max_length=1024 * 1024 * 8)
    type = serializers.ChoiceField(choices=Conference.ConferenceType)
    views_number = serializers.IntegerField()
    image = serializers.CharField(max_length=128)
    sliderFlag = serializers.BooleanField()
    create_time = serializers.DateTimeField()


class CreateConferenceSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=128)
    content = serializers.CharField(max_length=1024 * 1024 * 8)
    type = serializers.ChoiceField(choices=Conference.ConferenceType)
    image = serializers.CharField(max_length=128)
    sliderFlag = serializers.BooleanField()


class ConferenceSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    news_id = serializers.IntegerField()
    title = serializers.CharField(max_length=128)
    content = serializers.CharField(max_length=1024 * 1024 * 8)
    type = serializers.ChoiceField(choices=Conference.ConferenceType)
    views_number = serializers.IntegerField()
    image = serializers.CharField(max_length=128)
    sliderFlag = serializers.BooleanField()
    create_time = serializers.DateTimeField()
