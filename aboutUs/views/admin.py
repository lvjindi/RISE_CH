from django.shortcuts import render

from aboutUs.models import AboutUs
from aboutUs.serializers import AboutUsSerializer
from account.decorators import super_admin_required, login_required
from utils.api.api import APIView


class AboutUsAdminAPI(APIView):
    # @validate_serializer(CreateConferenceSerializer)
    # @validate_serializer(CreateNewsSerializer)
    @super_admin_required
    def post(self, request):
        title = request.POST.get('title')
        content = request.POST.get('content')
        aboutUs = AboutUs.objects.create(title=title, content=content)
        aboutUs.save()
        return self.success(AboutUsSerializer(aboutUs).data)

    # @validate_serializer(CreateConferenceSerializer)
    @super_admin_required
    def put(self, request):
        data = request.data
        try:
            aboutUs = AboutUs.objects.get(id=data['id'])
            setattr(aboutUs, 'content', data['content'])
            setattr(aboutUs, 'title', data['title'])

            aboutUs.save()

            return self.success(AboutUsSerializer(aboutUs).data)
        except AboutUs.DoesNotExist:
            return self.error("AboutUs does not exist")

    @login_required
    def get(self, request):
        aboutUs_id = request.GET.get('id')
        if aboutUs_id:
            try:
                aboutUs = AboutUs.objects.get(id=aboutUs_id)
                return self.success(AboutUsSerializer(aboutUs).data)
            except AboutUs.DoesNotExist:
                return self.error("AboutUs does not exist")
        else:
            aboutUs = AboutUs.objects.all()
            return self.success(self.paginate_data(request, aboutUs, AboutUsSerializer))

    @super_admin_required
    def delete(self, request):
        aboutUs_id = request.GET.get('id')
        if aboutUs_id:
            aboutUs = AboutUs.objects.get(id=aboutUs_id)
            aboutUs.delete()
            return self.success()


class AboutUsManageAdminAPI(APIView):
    def get(self, request):
        return render(request, 'aboutUsManagement.html')
