from django.shortcuts import render

# Create your views here.
from research.models import Introduction, Projects, Reports, Publications
from research.serializers import IntroductionSerializer, PublicationSerializer, ReportSerializer, \
    ProjectListSerializer, ProjectDetailSerializer
from utils.api.api import APIView


class IntroductionAPI(APIView):
    def get(self, request):
        data = request.data
        try:
            research = Introduction.objects.get(id=1)
            if research:
                views_number = research.views_number + 1
                setattr(research, "views_number", views_number)
                # research.update(views_number=views_number)
                research.save()
                research.create_time = research.create_time.strftime('%Y-%m-%d')
                return self.success(IntroductionSerializer(research).data)
            else:
                return self.error('The research does not exist')
        except Introduction.DoesNotExist:
            return self.error('Introduction does not exist')


class ProjectListAPI(APIView):
    def get(self, request):
        projects = Projects.objects.all().order_by('id')
        for item in projects:
            item.abstract=item.abstract[:200]
        return self.success(self.paginate_data(request, projects, ProjectListSerializer))


class ProjectDetailAPI(APIView):
    def get(self, request):
        data = request.data
        try:
            project = Projects.objects.get(id=data['id'])
            views_number = project.views_number + 1
            setattr(project, 'views_number', views_number)
            project.save()
            project.create_time = project.create_time.strftime('%Y-%m-%d')
            return self.success(ProjectDetailSerializer(project).data)
        except Projects.DoesNotExist:
            return self.error('Project does not exist')


class PublicationAPI(APIView):
    def get(self, request):
        public_time = request.GET.get('year')
        if public_time:
            publications = Publications.objects.filter(public_time=public_time)
            return self.success(self.paginate_data(request, publications, PublicationSerializer))
        else:
            publications = Publications.objects.all()
            return self.success(self.paginate_data(request, publications, PublicationSerializer))


class ReportAPI(APIView):
    def get(self, request):
        report_year = request.GET.get('year')
        if report_year:
            try:
                reports = Reports.objects.filter(report_year=report_year)
                return self.success(self.paginate_data(request, reports, ReportSerializer))
            except Reports.DoesNotExist:
                return self.error("Reports does not exist")
        else:
            reports = Reports.objects.all()
            return self.success(self.paginate_data(request, reports, ReportSerializer))
