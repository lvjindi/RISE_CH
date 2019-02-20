from rest_framework import serializers

from research.models import Category, Publications, Reports


class IntroductionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=64)
    content = serializers.CharField(max_length=1024 * 1024 * 8)
    views_number = serializers.IntegerField(default=0)
    create_time = serializers.DateTimeField()


class EditIntroductionSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=64)
    content = serializers.CharField(max_length=1024 * 1024 * 8)


class ProjectDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=64)
    author = serializers.CharField(max_length=128)
    project_code=serializers.CharField(max_length=64)
    project_fund = serializers.CharField(max_length=64)
    project_schedule = serializers.CharField(max_length=32)
    other = serializers.CharField(max_length=128)
    abstract = serializers.CharField(max_length=1024 * 1024 * 8)
    keywords = serializers.CharField(max_length=256)
    views_number = serializers.IntegerField()
    create_time = serializers.DateTimeField()


class ProjectListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=64)
    author = serializers.CharField(max_length=128)
    project_fund = serializers.CharField(max_length=64)
    project_schedule = serializers.CharField(max_length=32)
    abstract = serializers.CharField(max_length=1024 * 1024 * 8)
    other = serializers.CharField(max_length=128)
    create_time = serializers.DateTimeField()


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publications
        exclude = ["last_update_time"]


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        exclude = ["last_update_time"]


class CreateResearchSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=64)
    content = serializers.CharField(max_length=1024 * 1024 * 8)


class CreateProjectSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=64)
    author = serializers.CharField(max_length=128)
    project_fund = serializers.CharField(max_length=64)
    project_schedule = serializers.CharField(max_length=32)
    other = serializers.CharField(max_length=128)
    abstract = serializers.CharField(max_length=1024 * 1024 * 8)


class CreatePublicationSerializer(serializers.Serializer):
    author = serializers.CharField(max_length=128)
    title = serializers.CharField(max_length=256)
    public_place = serializers.CharField(max_length=256)
    public_year = serializers.CharField(max_length=64)
    other = serializers.CharField(max_length=1024)


class CreateReportSerializer(serializers.Serializer):
    author = serializers.CharField(max_length=64)
    title = serializers.CharField(max_length=128)
    report_place = serializers.CharField(max_length=256)
    report_time = serializers.CharField(max_length=64)
    report_year = serializers.CharField(max_length=4)
    pdf_path = serializers.CharField(max_length=256)
