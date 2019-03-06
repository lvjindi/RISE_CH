from rest_framework import serializers


class LeaveSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=24)
    email = serializers.CharField(max_length=64)
    startTime = serializers.DateTimeField()
    endTime = serializers.DateTimeField()
    reason = serializers.CharField(max_length=128 * 128)
    status = serializers.CharField(max_length=10)
    create_time = serializers.DateTimeField()
