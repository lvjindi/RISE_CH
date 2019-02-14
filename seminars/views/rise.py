from django.shortcuts import render

# Create your views here.
from seminars.models import Seminars
from seminars.serializers import SeminarsListSerializer, SeminarsDetailSerializer
from utils.api.api import APIView


class SeminarsListAPI(APIView):
    def get(self, request):
        seminars_list = Seminars.objects.all()
        return self.success(self.paginate_data(request, seminars_list, SeminarsListSerializer))


class SeminarsDetailAPI(APIView):
    def get(self, request):
        data = request.data
        try:
            seminars = Seminars.objects.get(id=data['id'])
            views_number = seminars.views_number+1
            setattr(seminars, 'views_number', views_number)
            seminars.save()
            return self.success(SeminarsDetailSerializer(seminars).data)
        except Seminars.DoesNotExist:
            return self.error('Seminars does not exist')