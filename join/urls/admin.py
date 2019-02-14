from django.conf.urls import url

from join.views.admin import JoinAdminAPI, JoinManageAdminAPI

urlpatterns = [

    url(r"^join/?$", JoinAdminAPI.as_view(), name="join_admin_api"),
    url(r"^join_management/?$", JoinManageAdminAPI.as_view(), name="join_management_admin_api"),
]
