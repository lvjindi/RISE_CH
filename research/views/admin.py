from django.contrib import admin

# Register your models here.
from account.decorators import super_admin_required, login_required
from research.models import Introduction, Projects, Publications, Reports
from research.serializers import CreateResearchSerializer, IntroductionSerializer, EditIntroductionSerializer, \
    CreateProjectSerializer, ProjectSerializer, CreatePublicationSerializer, PublicationSerializer, \
    CreateReportSerializer, ReportSerializer
from utils.api.api import APIView, validate_serializer


class ResearchAdminAPI(APIView):
    # @validate_serializer(CreateResearchSerializer)
    @super_admin_required
    def post(self, request):
        "publish research"
        data = request.data
        research = Introduction.objects.create(research_category=data['research_category'],
                                               content=data['content'], title=data["title"])
        return self.success(IntroductionSerializer(research).data)

    # @validate_serializer(EditIntroductionSerializer)
    @super_admin_required
    def put(self, request):
        "edit research"
        data = request.data
        research = Introduction.objects.filter(id=data['id'])
        research.update(**data)
        return self.success(IntroductionSerializer(research).data)

    @login_required
    def get(self, request):
        research_category = request.GET.get('research_category')
        if research_category:
            try:
                research = Introduction.objects.get(research_category=research_category)
                return self.success(IntroductionSerializer(research).data)
            except Introduction.DoesNotExist:
                return self.error('Research does not exist')
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
        data = request.data
        project = Projects.objects.create(title=data['title'], author=data['author'],
                                          project_number=data['project_number'], project_fund=data['project_fund'],
                                          project_schedule=data['project_schedule'], other=data['other'],
                                          abstract=data['abstract'])
        return self.success(ProjectSerializer(project).data)

    # @validate_serializer(CreateProjectSerializer)
    @super_admin_required
    def put(self, request):
        'edit project'
        data = request.data
        project = Projects.objects.filter(id=data['id'])
        project.update(**data)
        return self.success(ProjectSerializer(project).data)

    @login_required
    def get(self, request):
        project_id = request.GET.get('id')
        if project_id:
            try:
                project = Projects.objects.get(id=project_id)
                return self.success(ProjectSerializer(project).data)
            except Projects.DoesNotExist:
                return self.error("Project does not exist")
        else:
            project = Projects.objects.all()
            return self.success(self.paginate_data(request, project, ProjectSerializer))

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
        data = request.data
        publication = Publications.objects.create(**data)
        return self.success(PublicationSerializer(publication).data)

    # @validate_serializer(CreatePublicationSerializer)
    @super_admin_required
    def put(self, request):
        'edit Publications'
        data = request.data
        publication = Publications.objects.filter(id=data['id'])
        publication.update(**data)
        return self.success(PublicationSerializer(publication).data)

    @login_required
    def get(self, request):
        'get Publications'
        publication_id = request.GET.get('id')
        public_year = request.GET.get('public_year')
        if publication_id:
            try:
                publication = Publications.objects.get(id=publication_id)
                return self.success(PublicationSerializer(publication).data)
            except Publications.DoesNotExist:
                return self.error("Publication does not exist")
        elif public_year:
            publications = Publications.objects.filter(public_year=public_year)
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
        data = request.data
        report = Reports.objects.create(**data)
        return self.success(ReportSerializer(report).data)

    # @validate_serializer(CreateReportSerializer)
    @super_admin_required
    def put(self, request):
        'edit report'
        data = request.data
        try:
            report = Reports.objects.get(id=data['id'])
        except Reports.DoesNotExist:
            self.error("Reports does not exist")
        for k, v in data.items:
            setattr(report, k, v)
        report.save()
        return self.success(ReportSerializer(report).data)

    @login_required
    def get(self, request):
        report_year = request.GET.get('report_year')
        report_id = request.GET.get('id')
        if report_id:
            try:
                report = Reports.objects.get(id=report_id)
                return self.success(ReportSerializer(report).data)
            except Reports.DoesNotExist:
                return self.error("Reports does not exist")
        elif report_year:
            report = Reports.objects.filter(report_year=report_year)
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
