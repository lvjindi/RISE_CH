from django.conf.urls import url

from seminars.views.admin import SeminarAdminAPI, SeminarManageAdminAPI

urlpatterns = [
    url(r"^seminar/?$", SeminarAdminAPI.as_view(), name="seminar_admin_api"),
    url(r"^seminar_management/?$", SeminarManageAdminAPI.as_view(), name="seminar_management_api"),

]
