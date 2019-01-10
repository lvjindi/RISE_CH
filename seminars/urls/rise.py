from django.conf.urls import url

from seminars.views.rise import SeminarsListAPI, SeminarsDetailAPI

urlpatterns = [
    url(r"^seminar/list/?$", SeminarsListAPI.as_view(), name="seminar_list_api"),
    url(r"^seminar/detail/?$", SeminarsDetailAPI.as_view(), name="seminar_detail_api"),

]