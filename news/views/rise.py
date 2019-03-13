from django.shortcuts import render

# Create your views here.
from news.models import News
from news.serializers import NewsListSerializer, NewsDetailSerializer
from utils.api.api import APIView


class NewsListAPI(APIView):
    def get(self, request):
        data = request.data
        news_list = News.objects.all()
        for item in news_list:
            item.create_time = item.create_time.strftime('%Y-%m-%d')
        return self.success(self.paginate_data(request, news_list, NewsListSerializer))


class NewsDetailAPI(APIView):
    def get(self, request):
        data = request.data
        try:
            news_detail = News.objects.get(id=data['id'])
            views_number = news_detail.views_number + 1
            setattr(news_detail, 'views_number', views_number)
            news_detail.save()
            news_detail.create_time = news_detail.create_time.strftime('%Y-%m-%d')
            return self.success(NewsDetailSerializer(news_detail).data)
        except News.DoesNotExist:
            return self.error('News does not exist')


class NewsLatestListAPI(APIView):
    def get(self, request):
        data = request.data
        news_list = News.objects.order_by('-create_time')
        latest_news = news_list[:5]
        for item in latest_news:
            item.create_time = item.create_time.strftime('%Y-%m-%d')
        return self.success(self.paginate_data(request, latest_news, NewsListSerializer))

# class ImportantNewsListAPI(APIView):
#     def get(self, request):
#         data = request.data
#         important_news = News.objects.filter(is_important=1)
#         return self.success(self.paginate_data(request, important_news, NewsListSerializer))
