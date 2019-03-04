# -*-coding:utf-8 -*-
from itertools import chain

from django.shortcuts import render

from people.models import Staff, Student, AdjunctProfessor
from people.serializers import StaffInfoSerializer, StaffDetailSerializer, StudentInfoSerializer, \
    StudentDetailSerializer, AdjunctProfessorInfoSerializer, AdjunctProfessorDetailSerializer
from utils.api.api import APIView


# Create your views here.

class StaffInfoAPI(APIView):
    def get(self, request):
        staff_list = Staff.objects.all()
        return self.success(self.paginate_data(request, staff_list, StaffInfoSerializer))


class StaffDetailAPI(APIView):
    def get(self, request):
        data = request.data
        try:
            staff_detail = Staff.objects.filter(id=data['id'])
            return self.success(self.paginate_data(request, staff_detail, StaffDetailSerializer))
        except Staff.DoesNotExist:
            return self.error("Staff does not exist")


class StudentInfoAPI(APIView):
    def get(self, request):
        student_type = request.GET.get('type')  # 学生类型（硕士，博士，本科）
        student_status = request.GET.get('graduateStatus')  # 学生状态（在读，毕业）
        if student_type and student_status:
            student_list = Student.objects.filter(type=student_type, graduateStatus=student_status)
        else:
            if student_type:
                student_list = Student.objects.filter(type=student_type)
            elif student_status:
                student_list = Student.objects.filter(graduateStatus=student_status)
            else:
                student_list = Student.objects.all()
        return self.success(self.paginate_data(request, student_list, StudentInfoSerializer))


class StudentDetailAPI(APIView):
    def get(self, request):
        data = request.data
        try:
            student_detail = Student.objects.filter(id=data['id'])
            return self.success(self.paginate_data(request, student_detail, StudentDetailSerializer))
        except Student.DoesNotExist:
            return self.error("Student does not exist")


class AdjunctProfessorInfoAPI(APIView):
    def get(self, request):
        adjunct_professor_list = AdjunctProfessor.objects.all()
        return self.success(self.paginate_data(request, adjunct_professor_list, AdjunctProfessorInfoSerializer))


class AdjunctProfessorDetailAPI(APIView):
    def get(self, request):
        data = request.data
        try:
            adjunct_professor_detail = AdjunctProfessor.objects.filter(id=data['id'])
            return self.success(self.paginate_data(request, adjunct_professor_detail, AdjunctProfessorDetailSerializer))
        except AdjunctProfessor.DoesNotExist:
            return self.error("AdjunctProfessor does not exist")
