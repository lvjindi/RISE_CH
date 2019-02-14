from django.shortcuts import render

from account.decorators import super_admin_required, login_required
from exchanges.models import Exchange
from exchanges.serializers import CreateExchangeSerializer, ExchangeSerializer
from news.models import News
from news.serializers import CreateNewsSerializer
from utils.api.api import APIView, validate_serializer


class ExchangeAdminAPI(APIView):
    # @validate_serializer(CreateExchangeSerializer)
    # @validate_serializer(CreateNewsSerializer)
    @super_admin_required
    def post(self, request):
        data = request.data
        exchange = Exchange.objects.create(**data)
        news = News.objects.create(**data)
        exchange.news_id = news.id
        exchange.save()
        return self.success(ExchangeSerializer(exchange).data)

    # @validate_serializer(CreateExchangeSerializer)
    @super_admin_required
    def put(self, request):
        data = request.data
        try:
            exchange = Exchange.objects.get(id=data['id'])
            news = News.objects.get(id=exchange.news_id)
            for k, v in data.items:
                setattr(exchange, k, v)
                setattr(news, k, v)
            exchange.save()
            news.save()
            return self.success(ExchangeSerializer(exchange).data)
        except Exchange.DoesNotExist:
            return self.error("Exchange does not exist")

    @login_required
    def get(self, request):
        exchange_id = request.GET.get('id')
        exchange_type = request.GET.get('type')
        if exchange_id:
            try:
                exchange = Exchange.objects.get(id=exchange_id)
                return self.success(ExchangeSerializer(exchange).data)
            except Exchange.DoesNotExist:
                return self.error("Exchange does not exist")
        elif exchange_type:
            exchange = Exchange.objects.filter(type=exchange_type)
            return self.success(self.paginate_data(request, exchange, ExchangeSerializer))
        else:
            exchange = Exchange.objects.all()
            return self.success(self.paginate_data(request, exchange, ExchangeSerializer))

    @super_admin_required
    def delete(self, request):
        exchange_id = request.GET.get('id')
        if exchange_id:
            exchange = Exchange.objects.get(id=exchange_id)
            news = News.objects.get(id=exchange.news_id)
            exchange.delete()
            news.delete()
            return self.success()


class ExchangeManageAdminAPI(APIView):
    def get(self, request):
        return render(request, 'exchangeManagement.html')
