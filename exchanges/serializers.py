from rest_framework import serializers

from exchanges.models import ExchangeType


class ExchangeListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    news_id = serializers.IntegerField()
    title = serializers.CharField(max_length=128)
    type = serializers.ChoiceField(choices=[ExchangeType.Missions, ExchangeType.Visitors])
    create_time = serializers.DateTimeField()


class ExchangeDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=128)
    news_id = serializers.IntegerField()
    content = serializers.CharField(max_length=1024 * 1024 * 8)
    type = serializers.ChoiceField(choices=[ExchangeType.Missions, ExchangeType.Visitors])
    views_number = serializers.IntegerField()
    image = serializers.CharField(max_length=128)
    sliderFlag = serializers.BooleanField()
    create_time = serializers.DateTimeField()


class CreateExchangeSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=128)
    content = serializers.CharField(max_length=1024 * 1024 * 8)
    type = serializers.ChoiceField(choices=[ExchangeType.Missions, ExchangeType.Visitors])
    image = serializers.CharField(max_length=128)
    sliderFlag = serializers.BooleanField()


class ExchangeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    news_id = serializers.IntegerField()
    title = serializers.CharField(max_length=128)
    content = serializers.CharField(max_length=1024 * 1024 * 8)
    type = serializers.ChoiceField(choices=[ExchangeType.Missions, ExchangeType.Visitors])
    views_number = serializers.IntegerField()
    image = serializers.CharField(max_length=128)
    sliderFlag = serializers.BooleanField()
