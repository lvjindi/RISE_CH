from django.conf.urls import url

from exchanges.views.admin import ExchangeAdminAPI, ExchangeManageAdminAPI

urlpatterns = [
    url(r"^exchange/?$", ExchangeAdminAPI.as_view(), name="exchange_admin_api"),
    url(r"^exchange_management/?$", ExchangeManageAdminAPI.as_view(), name="exchange_management_admin_api"),
]
