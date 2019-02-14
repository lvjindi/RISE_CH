from django.conf.urls import url

from people.views.admin import PeopleAdminAPI, PeopleManageAdminAPI

urlpatterns = [
    url(r"^people/?$", PeopleAdminAPI.as_view(), name="people_admin_api"),
    url(r"^people_management/?$", PeopleManageAdminAPI.as_view(), name="people_management_admin_api"),
]
