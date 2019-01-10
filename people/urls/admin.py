from django.conf.urls import url

from people.views.admin import PeopleAdminAPI

urlpatterns = [
    url(r"^people/?$", PeopleAdminAPI.as_view(), name="people_admin_api"),

]