from django.conf.urls import url

from people.views.rise import PeopleInfoAPI, PeopleDetailAPI

urlpatterns = [
    url(r"^people/info/?$", PeopleInfoAPI.as_view(), name="people_info_api"),
    url(r"^people/detail/?$", PeopleDetailAPI.as_view(), name="people_detail_api"),

]