from account.decorators import super_admin_required, login_required
from conference.models import Conference
from conference.serializers import CreateConferenceSerializer, ConferenceSerializer
from utils.api.api import APIView, validate_serializer


class ConferenceAdminAPI(APIView):
    @validate_serializer(CreateConferenceSerializer)
    @super_admin_required
    def post(self, request):
        data = request.data
        conference = Conference.objects.create(**data)
        return self.success(ConferenceSerializer(conference).data)

    @validate_serializer(CreateConferenceSerializer)
    @super_admin_required
    def put(self, request):
        data = request.data
        try:
            conference = Conference.objects.get(id=data['id'])
            for k, v in data.items:
                setattr(conference, k, v)
            conference.save()
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
                return self.success(ConferenceSerializer(conference).data)
            except Conference.DoesNotExist:
                return self.error("Conference does not exist")
        elif conference_type:
            conference = Conference.objects.filter(type=conference_type)
            return self.success(self.paginate_data(request, conference, ConferenceSerializer))
        else:
            conference = Conference.objects.all()
            return self.success(self.paginate_data(request, conference, ConferenceSerializer))

    @super_admin_required
    def delete(self, request):
        conference_id = request.GET.get('id')
        if conference_id:
            Conference.objects.filter(id=conference_id).delete()
            return self.success()
