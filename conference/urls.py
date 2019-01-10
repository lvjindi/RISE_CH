from django.conf.urls import url

from conference.views import ConferenceListAPI, ConferenceDetailAPI

urlpatterns = [
    url(r"^list/?$", ConferenceListAPI.as_view(), name="conference_list_api"),
    url(r"^detail/?$", ConferenceDetailAPI.as_view(), name="conference_detail_api"),

]
