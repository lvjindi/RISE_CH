from rest_framework import serializers


class NewsListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=128)
    is_important = serializers.BooleanField()
    create_time = serializers.DateTimeField()


class NewsDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=128)
    content = serializers.CharField(max_length=1024 * 1024 * 8)
    is_important = serializers.BooleanField()
    views_number = serializers.IntegerField()
    image = serializers.CharField(max_length=128)
    sliderFlag = serializers.BooleanField()

class CreateNewsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=128)
    content = serializers.CharField(max_length=1024 * 1024 * 8)
    is_important = serializers.BooleanField()
    image = serializers.CharField(max_length=128)
    sliderFlag = serializers.BooleanField()

