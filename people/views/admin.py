from django.contrib import admin

# Register your models here.


from account.decorators import super_admin_required, login_required
from people.models import People
from people.serializers import CreatePeopleSerializer, PeopleSerializer
from utils.api.api import APIView, validate_serializer


class PeopleAdminAPI(APIView):
    # @validate_serializer(CreatePeopleSerializer)
    @super_admin_required
    def post(self, request):
        "publish people "
        data = request.data
        people = People.objects.create(**data)
        return self.success(PeopleSerializer(people).data)

    # @validate_serializer(PeopleSerializer)
    @login_required
    def put(self, request):
        "edit people：1.超级管理员可以全部修改2.不是管理员只能修改自己的"
        data = request.data
        user = self.request.user
        people_id = data.pop('id')
        people = People.objects.filter(id=people_id)
        if request.user.username == people['name'] or user.is_super_admin():
            people.update(**data)
            return self.success(PeopleSerializer(people).data)
        else:
            return self.error('Don\'t have permission')

    @login_required
    def get(self, request):
        "超级管理员可以看到全部，其他只能看见自己的"
        user = self.request.user
        if user.is_super_admin():
            people_id = request.GET.get('id')
            if people_id:
                try:
                    people = People.objects.get(id=people_id)
                    return self.success(PeopleSerializer(people).data)
                except People.DoesNotExist:
                    return self.error("People does not exits")
            people = People.objects.all()
            return self.success(self.paginate_data(request, people, PeopleSerializer))
        else:
            people = People.objects.filter(name=user.username)
            if people:
                return self.success(self.paginate_data(request, people, PeopleSerializer))
            else:
                return self.error("You does not exits in people")

    @super_admin_required
    def delete(self, request):
        people_id = request.GET.get('id')
        if people_id:
            People.objects.filter(id=people_id).delete()
            return self.success()
