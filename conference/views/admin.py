from django.shortcuts import render

from account.decorators import super_admin_required, login_required
from conference.models import Conference
from conference.serializers import CreateConferenceSerializer, ConferenceSerializer
from news.models import News
from news.serializers import CreateNewsSerializer
from utils.api.api import APIView, validate_serializer


class ConferenceAdminAPI(APIView):
    # @validate_serializer(CreateConferenceSerializer)
    # @validate_serializer(CreateNewsSerializer)
    @super_admin_required
    def post(self, request):
        title = request.POST.get('title')
        content = request.POST.get('content')
        type = request.POST.get('subType')
        conference = Conference.objects.create(title=title, content=content, type=type)
        news = News.objects.create(title=title, content=content, type='conference')
        conference.news_id = news.id
        conference.save()
        return self.success(ConferenceSerializer(conference).data)

    # @validate_serializer(CreateConferenceSerializer)
    @super_admin_required
    def put(self, request):
        data = request.data
        try:
            conference = Conference.objects.get(id=data['id'])
            news = News.objects.get(id=conference.news_id)
            setattr(conference, 'content', data['content'])
            setattr(conference, 'title', data['title'])
            setattr(conference, 'type', data['type'])
            setattr(news, 'content', data['content'])
            setattr(news, 'title', data['title'])
            conference.save()
            news.save()
            return self.success(ConferenceSerializer(conference).data)
        except Conference.DoesNotExist:
            return self.error("Conference does not exist")

    @login_required
    def get(self, request):
        conference_id = request.GET.get('id')
        conference_type = request.GET.get('type')
        if conference_id:
            try:
                conference = Conference.objects.get(id=conference_id)
                conference.type = conference.get_type_display()
                return self.success(ConferenceSerializer(conference).data)
            except Conference.DoesNotExist:
                return self.error("Conference does not exist")
        elif conference_type:
            conference = Conference.objects.filter(type=conference_type)
            for item in conference:
                item.type = item.get_type_display()
            return self.success(self.paginate_data(request, conference, ConferenceSerializer))
        else:
            conference = Conference.objects.all()
            for item in conference:
                item.type = item.get_type_display()
            return self.success(self.paginate_data(request, conference, ConferenceSerializer))

    @super_admin_required
    def delete(self, request):
        conference_id = request.GET.get('id')
        if conference_id:
            conference = Conference.objects.get(id=conference_id)
            news = News.objects.get(id=conference.news_id)
            conference.delete()
            news.delete()
            return self.success()


class ConferenceManageAdminAPI(APIView):
    def get(self, request):
        return render(request, 'conferenceManagement.html')
