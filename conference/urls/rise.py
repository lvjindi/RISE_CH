from django.conf.urls import url

from conference.views.rise import ConferenceListAPI, ConferenceDetailAPI

urlpatterns = [
    url(r"^conference/list/?$", ConferenceListAPI.as_view(), name="conference_list_api"),
    url(r"^conference/detail/?$", ConferenceDetailAPI.as_view(), name="conference_detail_api"),

]