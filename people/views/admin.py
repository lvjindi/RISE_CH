from django.contrib import admin

# Register your models here.
from django.shortcuts import render

from account.decorators import super_admin_required, login_required
from people.models import People
from people.serializers import CreatePeopleSerializer, PeopleSerializer
from utils.api.api import APIView, validate_serializer


class PeopleAdminAPI(APIView):
    # @validate_serializer(CreatePeopleSerializer)
    @super_admin_required
    def post(self, request):
        "publish people "
        img = request.FILES.get('img')
        name = request.POST.get('name')
        status = request.POST.get('status')
        user_category = request.POST.get('user_category')
        office = request.POST.get('office')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        position = request.POST.get('position')
        degree = request.POST.get('degree')
        professionalTitle = request.POST.get('professionalTitle')
        area = request.POST.get('area')
        interesting = request.POST.get('interesting')
        biography = request.POST.get('biography')
        project = request.POST.get('project')
        achievement = request.POST.get('achievement')
        activity = request.POST.get('activity')
        publication = request.POST.get('publication')
        report = request.POST.get('report')

        people = People.objects.create(img=img, name=name, status=status, user_category=user_category, office=office,
                                       phone=phone, email=email, position=position, degree=degree,
                                       professionalTitle=professionalTitle, area=area, interesting=interesting,
                                       biography=biography, project=project, achievement=achievement,
                                       activity=activity, publication=publication, report=report)
        return self.success(PeopleSerializer(people).data)

    # @validate_serializer(PeopleSerializer)
    @login_required
    def put(self, request):
        "edit people：1.超级管理员可以全部修改2.不是管理员只能修改自己的"
        data = request.data
        user = self.request.user
        try:
            people = People.objects.get(id=data['id'])
            if request.user.username == data['name'] or user.is_super_admin():
                setattr(people, 'name', data['name'])
                setattr(people, 'status', data['status'])
                setattr(people, 'user_category', data['user_category'])
                setattr(people, 'office', data['office'])
                setattr(people, 'phone', data['phone'])
                setattr(people, 'email', data['email'])
                setattr(people, 'position', data['position'])
                setattr(people, 'degree', data['degree'])
                setattr(people, 'professionalTitle', data['professionalTitle'])
                setattr(people, 'area', data['area'])
                setattr(people, 'interesting', data['interesting'])
                setattr(people, 'biography', data['biography'])
                setattr(people, 'project', data['project'])
                setattr(people, 'achievement', data['achievement'])
                setattr(people, 'activity', data['activity'])
                setattr(people, 'publication', data['publication'])
                setattr(people, 'report', data['report'])
                people.save()
                return self.success(PeopleSerializer(people).data)
            else:
                return self.error('Don\'t have permission')
        except People.DoesNotExist:
            return self.error("People does not exist")

    @login_required
    def get(self, request):
        "超级管理员可以看到全部，其他只能看见自己的"
        user = self.request.user
        if user.is_super_admin():
            people_id = request.GET.get('id')
            people_type = request.GET.get('type')
            if people_id:
                try:
                    people = People.objects.get(id=people_id)
                    return self.success(PeopleSerializer(people).data)
                except People.DoesNotExist:
                    return self.error("People does not exits")
            elif people_type:
                people = People.objects.filter(user_category=people_type)
                return self.success(self.paginate_data(request, people, PeopleSerializer))
            else:
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


class PeopleManageAdminAPI(APIView):
    def get(self, request):
        return render(request, 'peopleManagement.html')


class PeoplePublicAdminAPI(APIView):
    def get(self, request):
        return render(request, 'peoplePublic.html')
