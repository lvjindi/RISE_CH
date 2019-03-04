from aboutUs.models import AboutUs
from aboutUs.serializers import AboutUsSerializer
from utils.api.api import APIView


class AboutUsDetailAPI(APIView):
    def get(self, request):
        data = request.data
        try:
            aboutUs = AboutUs.objects.get(id=data['id'])
            views_number = aboutUs.views_number + 1
            setattr(aboutUs, 'views_number', views_number)
            aboutUs.save()
            return self.success(AboutUsSerializer(aboutUs).data)
        except AboutUs.DoesNotExist:
            return self.error('AboutUs does not exist')
