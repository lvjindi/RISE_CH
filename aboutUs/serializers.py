from rest_framework import serializers


class AboutUsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=128)
    content = serializers.CharField(max_length=1024 * 1024 * 8)
    views_number = serializers.IntegerField()
    create_time = serializers.DateTimeField()
