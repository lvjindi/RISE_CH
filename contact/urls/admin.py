from django.conf.urls import url

from contact.views.admin import ContactAdminAPI, ContactManageAdminAPI

urlpatterns = [
    url(r"^contact/?$", ContactAdminAPI.as_view(), name="contact_detail_list_api"),
    url(r"^contact_management/?$", ContactManageAdminAPI.as_view(), name="contact_detail_list_api"),
]
