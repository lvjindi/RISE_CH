# -*-coding:utf-8 -*-
from django.shortcuts import render

from people.models import People
from people.serializers import PeopleInfoSerializer, PeopleDetailSerializer
from utils.api.api import APIView


# Create your views here.
class PeopleInfoAPI(APIView):
    def get(self, request):
        data = request.data
        people_list = People.objects.filter(user_category=data['user_category'], status=1)
        return self.success(self.paginate_data(request, people_list, PeopleInfoSerializer))


class PeopleDetailAPI(APIView):
    def get(self, request):
        data = request.data
        try:
            people_detail = People.objects.filter(id=data['id'])
            return self.success(self.paginate_data(request, people_detail, PeopleDetailSerializer))
        except People.DoesNotExist:
            return self.error("People does not exist")