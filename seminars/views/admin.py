from account.decorators import super_admin_required, login_required

from seminars.models import Seminars
from seminars.serializers import CreateSeminarsSerializer, SeminarsSerializer
from utils.api.api import APIView, validate_serializer


class SeminarAdminAPI(APIView):
    @validate_serializer(CreateSeminarsSerializer)
    @super_admin_required
    def post(self, request):
        data = request.data
        seminar = Seminars.objects.create(**data)
        return self.success(SeminarsSerializer(seminar).data)

    @validate_serializer(CreateSeminarsSerializer)
    @super_admin_required
    def put(self, request):
        data = request.data
        try:
            seminar = Seminars.objects.get(id=data['id'])
            for k, v in data.items:
                setattr(seminar, k, v)
            seminar.save()
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
            Seminars.objects.get(id=seminar_id).delete()
            return self.success()
