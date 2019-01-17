from rest_framework import serializers


class JoinListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    news_id = serializers.IntegerField()
    title = serializers.CharField(max_length=128)
    create_time = serializers.DateTimeField()


class JoinDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    news_id = serializers.IntegerField()
    title = serializers.CharField(max_length=128)
    content = serializers.CharField(max_length=1024 * 1024 * 8)
    views_number = serializers.IntegerField()
    image = serializers.CharField(max_length=128)
    sliderFlag = serializers.BooleanField()
    create_time = serializers.DateTimeField()


class CreateJoinSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=128)
    content = serializers.CharField(max_length=1024 * 1024 * 8)
    image = serializers.CharField(max_length=128)
    sliderFlag = serializers.BooleanField()
