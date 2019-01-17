from django.conf.urls import url

from exchanges.views.admin import ExchangeAdminAPI

urlpatterns = [
    url(r"^exchange/?$", ExchangeAdminAPI.as_view(), name="exchange_admin_api"),

]