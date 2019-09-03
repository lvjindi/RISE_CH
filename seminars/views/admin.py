from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from account.decorators import super_admin_required, login_required
from news.models import News
from news.serializers import CreateNewsSerializer

from seminars.models import Seminars
from seminars.serializers import CreateSeminarsSerializer, SeminarsSerializer
from utils.api.api import APIView, validate_serializer


class SeminarAdminAPI(APIView):
    @csrf_exempt
    # @validate_serializer(CreateSeminarsSerializer)
    # @validate_serializer(CreateNewsSerializer)
    @super_admin_required
    def post(self, request):
        title = request.POST.get('title')
        content = request.POST.get('content')
        place = request.POST.get('place')
        time = request.POST.get('time')
        speaker = request.POST.get('speaker')
        create_time = request.POST.get('create_time')
        if create_time == '':
            seminar = Seminars.objects.create(title=title, content=content, place=place, time=time, speaker=speaker)
        else:
            seminar = Seminars.objects.create(title=title, content=content, place=place, time=time, speaker=speaker,
                                              create_time=create_time)
        news = News.objects.create(title=title, content=content, type='seminar', create_time=create_time)
        seminar.news_id = news.id
        seminar.save()
        return self.success(SeminarsSerializer(seminar).data)

    # @validate_serializer(CreateSeminarsSerializer)
    # @validate_serializer(CreateNewsSerializer)
    @super_admin_required
    def put(self, request):
        data = request.data
        try:
            seminar = Seminars.objects.get(id=data['id'])
            news = News.objects.get(id=seminar.news_id)
            setattr(seminar, 'place', data['place'])
            setattr(seminar, 'speaker', data['speaker'])
            setattr(seminar, 'title', data['title'])
            setattr(seminar, 'content', data['content'])
            setattr(seminar, 'create_time', data['create_time'])
            setattr(news, 'title', data['title'])
            setattr(news, 'content', data['content'])
            setattr(news, 'create_time', data['create_time'])
            seminar.save()
            news.save()
            return self.success(SeminarsSerializer(seminar).data)
        except Seminars.DoesNotExist:
            return self.error("Seminar does not exist")

    @login_required
    def get(self, request):
        seminar_id = request.GET.get('id')
        if seminar_id:
            try:
                seminar = Seminars.objects.get(id=seminar_id)
                return self.success(SeminarsSerializer(seminar).data)
            except Seminars.DoesNotExist:
                return self.error("Seminar does not exist")
        else:
            seminar = Seminars.objects.all()
            return self.success(self.paginate_data(request, seminar, SeminarsSerializer))

    @super_admin_required
    def delete(self, request):
        seminar_id = request.GET.get('id')
        if seminar_id:
            seminars = Seminars.objects.get(id=seminar_id)
            news = News.objects.get(id=seminars.news_id)
            seminars.delete()
            news.delete()
            return self.success()


class SeminarManageAdminAPI(APIView):
    def get(self, request):
        return render(request, 'seminarsManagement.html')
