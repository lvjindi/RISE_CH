from django.shortcuts import render

from account.decorators import super_admin_required, login_required
from news.models import News
from news.serializers import CreateNewsSerializer

from seminars.models import Seminars
from seminars.serializers import CreateSeminarsSerializer, SeminarsSerializer
from utils.api.api import APIView, validate_serializer


class SeminarAdminAPI(APIView):
    @validate_serializer(CreateSeminarsSerializer)
    @validate_serializer(CreateNewsSerializer)
    @super_admin_required
    def post(self, request):
        data = request.data
        seminar = Seminars.objects.create(**data)
        news = News.objects.create(**data)
        seminar.news_id = news.id
        seminar.save()
        return self.success(SeminarsSerializer(seminar).data)

    @validate_serializer(CreateSeminarsSerializer)
    @validate_serializer(CreateNewsSerializer)
    @super_admin_required
    def put(self, request):
        data = request.data
        try:
            seminar = Seminars.objects.get(id=data['id'])
            news = News.objects.get(id=seminar.news_id)
            for k, v in data.items:
                setattr(seminar, k, v)
                setattr(news, k, v)
            seminar.save()
            news.save()
            return self.success(SeminarsSerializer(seminar).data)
        except Seminars.DoesNotExist:
            return self.error("Seminar does not exist")

    # def get(self, request):
    #     return render(request, 'seminars.html')

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
