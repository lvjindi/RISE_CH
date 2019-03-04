from django.conf.urls import url

from people.views.rise import StaffInfoAPI, StaffDetailAPI, StudentInfoAPI, StudentDetailAPI, AdjunctProfessorInfoAPI, \
    AdjunctProfessorDetailAPI

urlpatterns = [
    url(r"^people/staff/info/?$", StaffInfoAPI.as_view(), name="people_staff_info_api"),
    url(r"^people/staff/detail/?$", StaffDetailAPI.as_view(), name="people_staff_detail_api"),
    url(r"^people/student/info/?$", StudentInfoAPI.as_view(), name="people_student_info_api"),
    url(r"^people/student/detail/?$", StudentDetailAPI.as_view(), name="people_student_detail_api"),
    url(r"^people/adjunctProfessor/info/?$", AdjunctProfessorInfoAPI.as_view(),
        name="people_adjunctProfessor_info_api"),
    url(r"^people/adjunctProfessor/detail/?$", AdjunctProfessorDetailAPI.as_view(),
        name="people_adjunctProfessor_detail_api"),

]
