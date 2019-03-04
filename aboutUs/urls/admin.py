from django.conf.urls import url

from aboutUs.views.admin import AboutUsAdminAPI, AboutUsManageAdminAPI

urlpatterns = [
    url(r"^aboutUs/?$", AboutUsAdminAPI.as_view(), name="aboutUs_detail_list_api"),
    url(r"^aboutUs_management/?$", AboutUsManageAdminAPI.as_view(), name="aboutUs_detail_list_api"),
]
