from django.shortcuts import render

# Create your views here.
from conference.models import Conference
from conference.serializers import ConferenceListSerializer, ConferenceDetailSerializer
from utils.api.api import APIView


class ConferenceListAPI(APIView):
    def get(self, request):
        data = request.data
        if data.get('type') == None:
            conference_list = Conference.objects.all()
            return self.success(self.paginate_data(request, conference_list, ConferenceListSerializer))
        else:
            conference_list = Conference.objects.filter(type=data['type'])
            return self.success(self.paginate_data(request, conference_list, ConferenceListSerializer))


class ConferenceDetailAPI(APIView):
    def get(self, request):
        data = request.data
        try:
            conference = Conference.objects.get(id=data['id'])
            views_number = conference.views_number + 1
            setattr(conference, 'views_number', views_number)
            conference.save()
            return self.success(ConferenceDetailSerializer(conference).data)
        except Conference.DoesNotExist:
            return self.error('Conference does not exist')
