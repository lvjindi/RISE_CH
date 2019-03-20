from django.contrib import admin

# Register your models here.
from django.shortcuts import render

from account.decorators import super_admin_required, login_required
from research.models import Introduction, Projects, Publications, Reports
from research.serializers import CreateResearchSerializer, IntroductionSerializer, EditIntroductionSerializer, \
    CreateProjectSerializer, CreatePublicationSerializer, PublicationSerializer, \
    CreateReportSerializer, ReportSerializer, ProjectDetailSerializer
from utils.api.api import APIView, validate_serializer


class ResearchAdminAPI(APIView):
    # @validate_serializer(CreateResearchSerializer)
    @super_admin_required
    def post(self, request):
        "publish research"
        title = request.POST.get('title')
        content = request.POST.get('content')
        research = Introduction.objects.create(title=title, content=content)
        return self.success(IntroductionSerializer(research).data)

    # @validate_serializer(EditIntroductionSerializer)
    @super_admin_required
    def put(self, request):
        "edit research"
        data = request.data
        try:
            introduction = Introduction.objects.get(id=data['id'])
            setattr(introduction, 'title', data['title'])
            setattr(introduction, 'content', data['content'])
            introduction.save()
            return self.success(IntroductionSerializer(introduction).data)
        except Introduction.DoesNotExist:
            return self.error("Seminar does not exist")

    @login_required
    def get(self, request):
        introduction_id = request.GET.get('id')
        if introduction_id:
            try:
                research = Introduction.objects.get(id=introduction_id)
                return self.success(IntroductionSerializer(research).data)
            except Introduction.DoesNotExist:
                return self.error('Introduction does not exist')
        else:
            research = Introduction.objects.all()
        return self.success(self.paginate_data(request, research, IntroductionSerializer))

    @super_admin_required
    def delete(self, request):
        research_id = request.GET.get('id')
        if research_id:
            Introduction.objects.filter(id=research_id).delete()
            return self.success()


class ProjectAdminAPI(APIView):
    # @validate_serializer(CreateProjectSerializer)
    @super_admin_required
    def post(self, request):
        'publish project'
        title = request.POST.get('title')
        author = request.POST.get('author')
        code = request.POST.get('code')
        fund = request.POST.get('fund')
        schedule = request.POST.get('schedule')
        other = request.POST.get('other')
        abstract = request.POST.get('abstract')
        keywords = request.POST.get('keywords')
        project = Projects.objects.create(title=title, author=author,
                                          project_code=code, project_fund=fund,
                                          project_schedule=schedule, other=other,
                                          abstract=abstract, keywords=keywords)
        return self.success(ProjectDetailSerializer(project).data)

    # @validate_serializer(CreateProjectSerializer)
    @super_admin_required
    def put(self, request):
        'edit project'
        data = request.data
        try:
            project = Projects.objects.get(id=data['id'])
            setattr(project, 'title', data['title'])
            setattr(project, 'author', data['author'])
            setattr(project, 'project_code', data['code'])
            setattr(project, 'project_fund', data['fund'])
            setattr(project, 'project_schedule', data['schedule'])
            setattr(project, 'abstract', data['abstract'])
            setattr(project, 'keywords', data['keywords'])
            setattr(project, 'other', data['other'])
            project.save()
            return self.success(ProjectDetailSerializer(project).data)
        except Projects.DoesNotExist:
            return self.error("Project does not exist")

    @login_required
    def get(self, request):
        project_id = request.GET.get('id')
        if project_id:
            try:
                project = Projects.objects.get(id=project_id)
                return self.success(ProjectDetailSerializer(project).data)
            except Projects.DoesNotExist:
                return self.error("Project does not exist")
        else:
            project = Projects.objects.all()
            return self.success(self.paginate_data(request, project, ProjectDetailSerializer))

    @super_admin_required
    def delete(self, request):
        project_id = request.GET.get('id')
        if project_id:
            Projects.objects.filter(id=project_id).delete()
            return self.success()


class PublicationAdminAPI(APIView):
    # @validate_serializer(CreatePublicationSerializer)
    @super_admin_required
    def post(self, request):
        'publish Publications'
        title = request.POST.get('title')
        author = request.POST.get('author')
        place = request.POST.get('place')
        year = request.POST.get('year')
        other = request.POST.get('other')
        publication = Publications.objects.create(title=title, author=author, place=place, year=year, other=other)
        return self.success(PublicationSerializer(publication).data)

    # @validate_serializer(CreatePublicationSerializer)
    @super_admin_required
    def put(self, request):
        'edit Publications'
        data = request.data
        try:
            publication = Publications.objects.get(id=data['id'])
            setattr(publication, 'title', data['title'])
            setattr(publication, 'author', data['author'])
            setattr(publication, 'place', data['place'])
            setattr(publication, 'year', data['year'])
            setattr(publication, 'other', data['other'])
            publication.save()
            return self.success(PublicationSerializer(publication).data)
        except Publications.DoesNotExist:
            return self.error("Publication does not exist")

    @login_required
    def get(self, request):
        'get Publications'
        publication_id = request.GET.get('id')
        public_year = request.GET.get('year')
        if publication_id:
            try:
                publication = Publications.objects.get(id=publication_id)
                return self.success(PublicationSerializer(publication).data)
            except Publications.DoesNotExist:
                return self.error("Publication does not exist")
        elif public_year:
            publications = Publications.objects.filter(year=public_year)
            return self.success(self.paginate_data(request, publications, PublicationSerializer))
        else:
            publications = Publications.objects.all()
            return self.success(self.paginate_data(request, publications, PublicationSerializer))

    @super_admin_required
    def delete(self, request):
        publication_id = request.GET.get('id')
        if publication_id:
            Publications.objects.filter(id=publication_id).delete()
            return self.success()


class ReportAdminAPI(APIView):
    # @validate_serializer(CreateReportSerializer)
    @super_admin_required
    def post(self, request):
        'publish report'
        pdf = request.FILES.get('pdf')
        title = request.POST.get('title')
        author = request.POST.get('author')
        place = request.POST.get('place')
        year = request.POST.get('year')
        other = request.POST.get('other')
        time = request.POST.get('time')
        report = Reports.objects.create(title=title, author=author, place=place, time=time, year=year, other=other,
                                        pdf_path=pdf)
        return self.success(ReportSerializer(report).data)

    # @validate_serializer(CreateReportSerializer)
    @super_admin_required
    def put(self, request):
        'edit report'
        data = request.data
        try:
            report = Reports.objects.get(id=data['id'])
            setattr(report, 'title', data['title'])
            setattr(report, 'author', data['author'])
            setattr(report, 'place', data['place'])
            setattr(report, 'time', data['time'])
            setattr(report, 'pdf_path', data['pdf'])
            setattr(report, 'year', data['year'])
            setattr(report, 'other', data['other'])
            report.save()
            return self.success(ReportSerializer(report).data)
        except Reports.DoesNotExist:
            return self.error("Report does not exist")

    @login_required
    def get(self, request):
        report_year = request.GET.get('year')
        report_id = request.GET.get('id')
        if report_id:
            try:
                report = Reports.objects.get(id=report_id)
                return self.success(ReportSerializer(report).data)
            except Reports.DoesNotExist:
                return self.error("Reports does not exist")
        elif report_year:
            report = Reports.objects.filter(year=report_year)
            return self.success(self.paginate_data(request, report, ReportSerializer))
        else:
            report = Reports.objects.all()
            return self.success(self.paginate_data(request, report, ReportSerializer))

    @super_admin_required
    def delete(self, request):
        report_id = request.GET.get('id')
        if report_id:
            Reports.objects.get(id=report_id).delete()
            return self.success()


class ResearchManageAdminAPI(APIView):
    def get(self, request):
        return render(request, 'researchManagement.html')
