import os

from django.contrib import admin

# Register your models here.
from django.shortcuts import render

from Rise_CH import settings
from account.decorators import super_admin_required, login_required
from people.models import Staff, Student, AdjunctProfessor

from people.serializers import StaffSerializer, StudentSerializer, AdjunctProfessorSerializer
from utils.api.api import APIView, validate_serializer


class StaffAdminAPI(APIView):
    @login_required
    def post(self, request):
        "publish staff "
        img = request.FILES.get('img')
        if img is not None:
            imgPath = os.path.join(settings.MEDIA_URL, img.name.replace(' ', '_'))
        else:
            imgPath = ''
        name = request.POST.get('name')
        status = request.POST.get('status')
        office = request.POST.get('office')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        position = request.POST.get('position')
        degree = request.POST.get('degree')
        professionalTitle = request.POST.get('professionalTitle')
        profession = request.POST.get('profession')
        area = request.POST.get('area')
        interesting = request.POST.get('interesting')
        biography = request.POST.get('biography')
        project = request.POST.get('project')
        achievement = request.POST.get('achievement')
        activity = request.POST.get('activity')
        publication = request.POST.get('publication')
        report = request.POST.get('report')
        link = request.POST.get('link')
        staff = Staff.objects.create(img=img, imgPath=imgPath, name=name, status=status, office=office,
                                     phone=phone, email=email, position=position, degree=degree,
                                     professionalTitle=professionalTitle, profession=profession, area=area,
                                     interesting=interesting, biography=biography, project=project,
                                     achievement=achievement, activity=activity, publication=publication,
                                     report=report, link=link)
        return self.success(StaffSerializer(staff).data)

    @login_required
    def put(self, request):
        "edit staff：1.超级管理员可以全部修改2.不是管理员只能修改自己的"
        data = request.data
        user = self.request.user
        try:
            staff = Staff.objects.get(id=data['id'])
            if request.user.real_name == data['name'] or user.is_super_admin():
                setattr(staff, 'name', data['name'])
                setattr(staff, 'status', data['status'])
                setattr(staff, 'office', data['office'])
                setattr(staff, 'phone', data['phone'])
                setattr(staff, 'email', data['email'])
                setattr(staff, 'position', data['position'])
                setattr(staff, 'degree', data['degree'])
                setattr(staff, 'professionalTitle', data['professionalTitle'])
                setattr(staff, 'profession', data['profession'])
                setattr(staff, 'area', data['area'])
                setattr(staff, 'interesting', data['interesting'])
                setattr(staff, 'biography', data['biography'])
                setattr(staff, 'project', data['project'])
                setattr(staff, 'achievement', data['achievement'])
                setattr(staff, 'activity', data['activity'])
                setattr(staff, 'publication', data['publication'])
                setattr(staff, 'report', data['report'])
                staff.save()
                return self.success(StaffSerializer(staff).data)
            else:
                return self.error('Don\'t have permission')
        except Staff.DoesNotExist:
            return self.error("staff does not exist")

    @login_required
    def get(self, request):
        "超级管理员可以看到全部，其他只能看见自己的"
        user = self.request.user
        staff_id = request.GET.get('id')
        if user.is_super_admin():
            if staff_id:
                try:
                    staff = Staff.objects.get(id=staff_id)
                    staff.status = staff.get_status_display()
                    return self.success(StaffSerializer(staff).data)
                except Staff.DoesNotExist:
                    return self.error("Staff does not exits")
            else:
                staff = Staff.objects.all()
                for item in staff:
                    item.status = item.get_status_display()
                return self.success(self.paginate_data(request, staff, StaffSerializer))
        else:
            if not staff_id:
                staff = Staff.objects.filter(name=user.real_name)
                if staff:
                    for item in staff:
                        item.status = item.get_status_display()
                    return self.success(self.paginate_data(request, staff, StaffSerializer))
                else:
                    return self.error("You does not exits in staff")
            else:
                try:
                    staff = Staff.objects.get(id=staff_id)
                    staff.status = staff.get_status_display()
                    return self.success(StaffSerializer(staff).data)
                except Staff.DoesNotExist:
                    return self.error("Staff does not exits")

    @super_admin_required
    def delete(self, request):
        staff_id = request.GET.get('id')
        if staff_id:
            Staff.objects.filter(id=staff_id).delete()
            return self.success()


class StudentAdminAPI(APIView):
    @login_required
    def post(self, request):
        "publish student "
        img = request.FILES.get('img')
        if img is not None:
            imgPath = os.path.join(settings.MEDIA_URL, img.name.replace(' ', '_'))
        else:
            imgPath = ''
        name = request.POST.get('name')
        graduateStatus = request.POST.get('graduateStatus')
        email = request.POST.get('email')
        enrollmentTime = request.POST.get('enrollmentTime ')
        graduationTime = request.POST.get('graduationTime ')
        type = request.POST.get('type')
        supervisor = request.POST.get('supervisor')
        supervisorLink = request.POST.get('supervisorLink')
        area = request.POST.get('area')
        biography = request.POST.get('biography')
        project = request.POST.get('project')
        activity = request.POST.get('activity')
        publication = request.POST.get('publication')
        link = request.POST.get('link')
        student = Student.objects.create(img=img, imgPath=imgPath, name=name, graduateStatus=graduateStatus,
                                         email=email, enrollmentTime=enrollmentTime, graduationTime=graduationTime,
                                         type=type, area=area, supervisor=supervisor, biography=biography,
                                         project=project, supervisorLink=supervisorLink,
                                         activity=activity, publication=publication, link=link
                                         )
        return self.success(StudentSerializer(student).data)

    @login_required
    def put(self, request):
        "edit staff：1.超级管理员可以全部修改2.不是管理员只能修改自己的"
        data = request.data
        user = self.request.user
        try:
            student = Student.objects.get(id=data['id'])
            if request.user.real_name == data['name'] or user.is_super_admin():
                setattr(student, 'name', data['name'])
                setattr(student, 'graduateStatus', data['graduateStatus'])
                setattr(student, 'email', data['email'])
                setattr(student, 'area', data['area'])
                setattr(student, 'biography', data['biography'])
                setattr(student, 'project', data['project'])
                setattr(student, 'activity', data['activity'])
                setattr(student, 'publication', data['publication'])
                student.save()
                return self.success(StudentSerializer(student).data)
            else:
                return self.error('Don\'t have permission')
        except Student.DoesNotExist:
            return self.error("Student does not exist")

    @login_required
    def get(self, request):
        "超级管理员可以看到全部，其他只能看见自己的"
        user = self.request.user
        student_id = request.GET.get('id')
        student_type = request.GET.get('type')
        student_status = request.GET.get('graduateStatus')
        if user.is_super_admin():
            if student_id:
                try:
                    student = Student.objects.get(id=student_id)
                    student.type = student.get_type_display()
                    student.graduateStatus = student.get_graduateStatus_display()
                    student.supervisor = student.get_supervisor_display()
                    return self.success(StudentSerializer(student).data)
                except Student.DoesNotExist:
                    return self.error("Student does not exits")
            elif student_type and student_status:
                student = Student.objects.filter(type=student_type, graduateStatus=student_status)
            elif student_type:
                student = Student.objects.filter(type=student_type)
            elif student_status:
                student = Student.objects.filter(graduateStatus=student_status)
            else:
                student = Student.objects.all()
            for item in student:
                item.type = item.get_type_display()
                item.graduateStatus = item.get_graduateStatus_display()
                item.supervisor = item.get_supervisor_display()
            return self.success(self.paginate_data(request, student, StudentSerializer))
        else:
            if not student_id:
                student = Student.objects.filter(name=user.real_name)
                if student:
                    for item in student:
                        item.type = item.get_type_display()
                        item.graduateStatus = item.get_graduateStatus_display()
                        item.supervisor = item.get_supervisor_display()
                    return self.success(self.paginate_data(request, student, StudentSerializer))
                else:
                    return self.error("You does not exits in student")
            else:
                try:
                    student = Student.objects.get(id=student_id)
                    student.type = student.get_type_display()
                    student.graduateStatus = student.get_graduateStatus_display()
                    student.supervisor = student.get_supervisor_display()
                    return self.success(StudentSerializer(student).data)
                except Student.DoesNotExist:
                    return self.error("Student does not exits")

    @super_admin_required
    def delete(self, request):
        student_id = request.GET.get('id')
        if student_id:
            Student.objects.filter(id=student_id).delete()
            return self.success()


class AdjunctProfessorAdminAPI(APIView):
    @login_required
    def post(self, request):
        "publish adjunctProfessor"
        img = request.FILES.get('img')
        if img is not None:
            imgPath = os.path.join(settings.MEDIA_URL, img.name.replace(' ', '_'))
        else:
            imgPath = ''
        name = request.POST.get('name')
        email = request.POST.get('email')
        degree = request.POST.get('degree')
        professionalTitle = request.POST.get('professionalTitle')
        area = request.POST.get('area')
        biography = request.POST.get('biography')
        link = request.POST.get('link')
        adjunctProfessor = AdjunctProfessor.objects.create(img=img, imgPath=imgPath, name=name,
                                                           email=email, degree=degree,
                                                           professionalTitle=professionalTitle, area=area,
                                                           biography=biography, link=link
                                                           )
        return self.success(AdjunctProfessorSerializer(adjunctProfessor).data)

    @login_required
    def put(self, request):
        "edit staff：1.超级管理员可以全部修改2.不是管理员只能修改自己的"
        data = request.data
        user = self.request.user
        try:
            adjunctProfessor = AdjunctProfessor.objects.get(id=data['id'])
            if request.user.real_name == data['name'] or user.is_super_admin():
                setattr(adjunctProfessor, 'name', data['name'])
                setattr(adjunctProfessor, 'email', data['email'])
                setattr(adjunctProfessor, 'degree', data['degree'])
                setattr(adjunctProfessor, 'professionalTitle', data['professionalTitle'])
                setattr(adjunctProfessor, 'area', data['area'])
                setattr(adjunctProfessor, 'biography', data['biography'])
                setattr(adjunctProfessor, 'link', data['link'])
                adjunctProfessor.save()
                return self.success(AdjunctProfessorSerializer(adjunctProfessor).data)
            else:
                return self.error('Don\'t have permission')
        except AdjunctProfessor.DoesNotExist:
            return self.error("AdjunctProfessor does not exist")

    @login_required
    def get(self, request):
        "超级管理员可以看到全部，其他只能看见自己的"
        user = self.request.user
        adjunctProfessor_id = request.GET.get('id')
        if user.is_super_admin():
            if adjunctProfessor_id:
                try:
                    adjunctProfessor = AdjunctProfessor.objects.get(id=adjunctProfessor_id)
                    return self.success(AdjunctProfessorSerializer(adjunctProfessor).data)
                except AdjunctProfessor.DoesNotExist:
                    return self.error("AdjunctProfessor does not exits")
            else:
                adjunctProfessor = AdjunctProfessor.objects.all()
                return self.success(self.paginate_data(request, adjunctProfessor, AdjunctProfessorSerializer))
        else:
            if not adjunctProfessor_id:
                adjunctProfessor = AdjunctProfessor.objects.filter(name=user.real_name)
                if adjunctProfessor:
                    return self.success(self.paginate_data(request, adjunctProfessor, AdjunctProfessorSerializer))
                else:
                    return self.error("You does not exits in staff")
            else:
                try:
                    adjunctProfessor = AdjunctProfessor.objects.get(id=adjunctProfessor_id)
                    return self.success(StaffSerializer(adjunctProfessor).data)
                except AdjunctProfessor.DoesNotExist:
                    return self.error("AdjunctProfessor does not exits")

    @super_admin_required
    def delete(self, request):
        adjunctProfessor_id = request.GET.get('id')
        if adjunctProfessor_id:
            AdjunctProfessor.objects.filter(id=adjunctProfessor_id).delete()
            return self.success()


class StaffManageAdminAPI(APIView):
    def get(self, request):
        return render(request, 'staffManagement.html')


class StaffPublicAdminAPI(APIView):
    def get(self, request):
        return render(request, 'staffPublic.html')


class StudentPublicAdminAPI(APIView):
    def get(self, request):
        return render(request, 'studentPublic.html')


class StudentManageAdminAPI(APIView):
    def get(self, request):
        return render(request, 'studentManagement.html')


class AdjunctProfessorManageAdminAPI(APIView):
    def get(self, request):
        return render(request, 'adjunctProfessorManagement.html')


class AdjunctProfessorPublicAdminAPI(APIView):
    def get(self, request):
        return render(request, 'adjunctProfessorPublic.html')
