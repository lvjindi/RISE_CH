from django.conf.urls import url

from join.views.admin import JoinAdminAPI

urlpatterns = [

    url(r"^join/?$", JoinAdminAPI.as_view(), name="join_admin_api"),

]