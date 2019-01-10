from django.shortcuts import render

# Create your views here.
from join.models import Join
from join.serializers import JoinListSerializer, JoinDetailSerializer
from utils.api.api import APIView


class JoinListAPI(APIView):
    def get(self, request):
        data = request.data
        join_list = Join.objects.all()
        return self.success(self.paginate_data(request, join_list, JoinListSerializer))


class JoinDetailAPI(APIView):
    def get(self, request):
        data = request.data
        try:
            join_detail = Join.objects.get(id=data['id'])
            views_number = join_detail.views_number + 1
            setattr(join_detail, 'views_number', views_number)
            join_detail.save()
            return self.success(JoinDetailSerializer(join_detail).data)
        except Join.DoesNotExist:
            return self.error('News does not exist')
