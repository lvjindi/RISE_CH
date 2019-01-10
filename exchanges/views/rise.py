from django.shortcuts import render

# Create your views here.
from exchanges.models import Exchange
from exchanges.serializers import ExchangeListSerializer, ExchangeDetailSerializer
from utils.api.api import APIView


class ExchangeListAPI(APIView):
    def get(self, request):
        data = request.data
        if data.get('type') == None:
            exchange_list = Exchange.objects.all()
            return self.success(self.paginate_data(request, exchange_list, ExchangeListSerializer))
        else:
            exchange_list = Exchange.objects.filter(type=data['type'])
            return self.success(self.paginate_data(request, exchange_list, ExchangeListSerializer))


class ExchangeDetailAPI(APIView):
    def get(self, request):
        data = request.data
        try:
            exchange_detail = Exchange.objects.get(id=data['id'])
            views_number = exchange_detail.views_number + 1
            setattr(exchange_detail, 'views_number', views_number)
            exchange_detail.save()
            return self.success(self.paginate_data(request, exchange_detail, ExchangeDetailSerializer))
        except Exchange.DoesNotExist:
            return self.error('Exchange does not exist')
