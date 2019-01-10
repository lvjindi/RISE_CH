from django.conf.urls import url

from exchanges.views.rise import ExchangeListAPI, ExchangeDetailAPI

urlpatterns = [
    url(r"^exchange/list/?$", ExchangeListAPI.as_view(), name="exchange_list_api"),
    url(r"^exchange/detail/?$", ExchangeDetailAPI.as_view(), name="exchange_detail_api"),

]