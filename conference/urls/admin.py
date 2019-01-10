from django.conf.urls import url

from conference.views.admin import ConferenceAdminAPI

urlpatterns = [
    url(r"^conference/?$", ConferenceAdminAPI.as_view(), name="conference_admin_api"),

]