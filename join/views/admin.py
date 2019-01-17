from django.shortcuts import render

from account.decorators import super_admin_required, login_required
from join.models import Join
from join.serializers import CreateJoinSerializer, JoinDetailSerializer
from news.models import News
from news.serializers import CreateNewsSerializer
from utils.api.api import APIView, validate_serializer


class JoinAdminAPI(APIView):
    @validate_serializer(CreateJoinSerializer)
    @validate_serializer(CreateNewsSerializer)
    @super_admin_required
    def post(self, request):
        data = request.data
        join = Join.objects.create(**data)
        news = News.objects.create(**data)
        join.news_id = news.id
        join.save()
        return self.success(JoinDetailSerializer(join).data)

    @validate_serializer(CreateJoinSerializer)
    @super_admin_required
    def put(self, request):
        data = request.data
        try:
            join = Join.objects.get(id=data['id'])
            news = News.objects.get(id=join.news_id)
            for k, v in data.items:
                setattr(join, k, v)
                setattr(news, k, v)
            join.save()
            news.save()
            return self.success(JoinDetailSerializer(join).data)
        except Join.DoesNotExist:
            return self.error("Join does not exist")


    @login_required
    def get(self, request):
        join_id = request.GET.get('id')
        if join_id:
            try:
                join = Join.objects.get(id=join_id)
                return self.success(JoinDetailSerializer(join).data)
            except Join.DoesNotExist:
                return self.error("Join dose not exist")
        else:
            join = Join.objects.all()
            return self.success(self.paginate_data(request, join, JoinDetailSerializer))

    @super_admin_required
    def delete(self, request):
        join_id = request.GET.get('id')
        if join_id:
            join = Join.objects.get(id=join_id)
            news = News.objects.get(id=join.news_id)
            join.delete()
            news.delete()
            return self.success()
