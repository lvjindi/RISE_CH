from rest_framework import serializers

from seminars.models import Seminars


class SeminarsListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    news_id = serializers.IntegerField()
    title = serializers.CharField(max_length=128)
    create_time = serializers.DateTimeField()


class SeminarsDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    news_id = serializers.IntegerField()
    content = serializers.CharField(max_length=1024 * 1024 * 8)
    views_number = serializers.IntegerField()
    image = serializers.CharField(max_length=128)
    sliderFlag = serializers.BooleanField()


class SeminarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seminars
        exclude = ["last_update_time"]


class CreateSeminarsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=128)
    content = serializers.CharField(max_length=1024 * 1024 * 8)
    image = serializers.CharField(max_length=128)
    sliderFlag = serializers.BooleanField()
