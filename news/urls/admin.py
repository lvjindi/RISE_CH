from django.conf.urls import url

from news.views.admin import NewsAdminAPI, NewsPublicAdminAPI, NewsManageAdminAPI

urlpatterns = [
    url(r"^news/?$", NewsAdminAPI.as_view(), name="news_admin_api"),
    url(r"^news_public/?$", NewsPublicAdminAPI.as_view(), name="news_public_admin_api"),
    url(r"^news_management/?$", NewsManageAdminAPI.as_view(), name="news_management_admin_api"),
]
