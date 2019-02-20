from rest_framework import serializers

from seminars.models import Seminars


class SeminarsListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    news_id = serializers.IntegerField()
    title = serializers.CharField(max_length=128)
    views_number = serializers.IntegerField()
    create_time = serializers.DateTimeField()


class SeminarsDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    news_id = serializers.IntegerField()
    title = serializers.CharField(max_length=128)
    content = serializers.CharField(max_length=1024 * 1024 * 8)
    views_number = serializers.IntegerField()
    image = serializers.ImageField()
    sliderFlag = serializers.BooleanField()
    create_time = serializers.DateTimeField()


class SeminarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seminars
        exclude = ["last_update_time"]


class CreateSeminarsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=128)
    content = serializers.CharField(max_length=1024 * 1024 * 8)
    image = serializers.ImageField()
    sliderFlag = serializers.BooleanField()
