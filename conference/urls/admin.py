from django.conf.urls import url

from conference.views.admin import ConferenceAdminAPI, ConferenceManageAdminAPI

urlpatterns = [
    url(r"^conference/?$", ConferenceAdminAPI.as_view(), name="conference_admin_api"),
    url(r"^conference_management/?$", ConferenceManageAdminAPI.as_view(), name="conference_management_admin_api"),
]
