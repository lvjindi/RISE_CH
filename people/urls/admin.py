from django.conf.urls import url

from people.views.admin import StaffAdminAPI, StudentAdminAPI, AdjunctProfessorAdminAPI, StaffManageAdminAPI, \
    StaffPublicAdminAPI, StudentPublicAdminAPI, StudentManageAdminAPI, AdjunctProfessorPublicAdminAPI, \
    AdjunctProfessorManageAdminAPI

urlpatterns = [
    url(r"^people/staff?$", StaffAdminAPI.as_view(), name="people_staff_admin_api"),
    url(r"^people/student?$", StudentAdminAPI.as_view(), name="people_student_admin_api"),
    url(r"^people/adjunctProfessor?$", AdjunctProfessorAdminAPI.as_view(), name="people_adjunct_professor_admin_api"),
    url(r"^people/staff_management/?$", StaffManageAdminAPI.as_view(), name="staff_management_admin_api"),
    url(r"^people/staff_public/?$", StaffPublicAdminAPI.as_view(), name="staff_public_admin_api"),
    url(r"^people/student_public/?$", StudentPublicAdminAPI.as_view(), name="student_public_admin_api"),
    url(r"^people/student_management/?$", StudentManageAdminAPI.as_view(), name="student_management_admin_api"),
    url(r"^people/adjunctProfessor_public/?$", AdjunctProfessorPublicAdminAPI.as_view(),
        name="adjunct_professor_public_admin_api"),
    url(r"^people/adjunctProfessor_management/?$", AdjunctProfessorManageAdminAPI.as_view(),
        name="adjunct_professor_management_admin_api"),
]
