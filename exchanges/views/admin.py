from account.decorators import super_admin_required, login_required
from exchanges.models import Exchange
from exchanges.serializers import CreateExchangeSerializer, ExchangeSerializer
from utils.api.api import APIView, validate_serializer


class ExchangeAdminAPI(APIView):
    @validate_serializer(CreateExchangeSerializer)
    @super_admin_required
    def post(self, request):
        data = request.data
        exchange = Exchange.objects.create(**data)
        return self.success(ExchangeSerializer(exchange).data)

    @validate_serializer(CreateExchangeSerializer)
    @super_admin_required
    def put(self, request):
        data = request.data
        try:
            exchange = Exchange.objects.get(id=data['id'])
            for k, v in data.items:
                setattr(exchange, k, v)
            exchange.save()
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
            Exchange.objects.filter(id=exchange_id).delete()
            return self.success()
