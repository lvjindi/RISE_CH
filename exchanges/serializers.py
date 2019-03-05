from rest_framework import serializers

from exchanges.models import Exchange


class ExchangeListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    news_id = serializers.IntegerField()
    title = serializers.CharField(max_length=128)
    type = serializers.ChoiceField(choices=Exchange.ExchangeType)
    create_time = serializers.DateTimeField()


class ExchangeDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=128)
    news_id = serializers.IntegerField()
    content = serializers.CharField(max_length=1024 * 1024 * 8)
    type = serializers.ChoiceField(choices=Exchange.ExchangeType)
    views_number = serializers.IntegerField()
    image = serializers.CharField(max_length=128)
    sliderFlag = serializers.BooleanField()
    create_time = serializers.DateTimeField()


class ExchangeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    news_id = serializers.IntegerField()
    title = serializers.CharField(max_length=128)
    content = serializers.CharField(max_length=1024 * 1024 * 8)
    type = serializers.ChoiceField(choices=Exchange.ExchangeType)
    views_number = serializers.IntegerField()
    image = serializers.CharField(max_length=128)
    sliderFlag = serializers.BooleanField()
    create_time = serializers.DateTimeField()
