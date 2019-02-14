from django.shortcuts import render

from account.decorators import super_admin_required, login_required
from news.models import News
from news.serializers import CreateNewsSerializer, NewsDetailSerializer
from utils.api.api import APIView, validate_serializer


class NewsAdminAPI(APIView):
    # @validate_serializer(CreateNewsSerializer)
    @super_admin_required
    def post(self, request):
        data = request.data
        news = News.objects.create(**data)
        return self.success(NewsDetailSerializer(news).data)

    # @validate_serializer(CreateNewsSerializer)
    @super_admin_required
    def put(self, request):
        data = request.data
        try:
            news = News.objects.get(id=data['id'])
            for k, v in data.items:
                setattr(news, k, v)
            news.save()
            return self.success(NewsDetailSerializer(news).data)
        except News.DoesNotExist:
            return self.error("News does not exist")

    @login_required
    def get(self, request):
        news_id = request.GET.get('id')
        if news_id:
            try:
                news = News.objects.get(id=news_id)
                return self.success(NewsDetailSerializer(news).data)
            except News.DoesNotExist:
                return self.error("News does not exist")
        else:
            news = News.objects.all()
            return self.success(self.paginate_data(request, news, NewsDetailSerializer))

    @super_admin_required
    def delete(self, request):
        news_id = request.GET.get('id')
        if news_id:
            News.objects.filter(id=news_id).delete()
            return self.success()


class NewsPublicAdminAPI(APIView):
    def get(self, request):
        return render(request, 'newsPublic.html')


class NewsManageAdminAPI(APIView):
    def get(self, request):
        return render(request, 'newsMangement.html')
