from django.conf.urls import url

from join.views.rise import JoinListAPI, JoinDetailAPI

urlpatterns = [
    url(r"^join/list/?$", JoinListAPI.as_view(), name="join_list_api"),
    url(r"^join/detail/?$", JoinDetailAPI.as_view(), name="join_detail_api"),

]