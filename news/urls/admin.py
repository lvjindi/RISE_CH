from django.conf.urls import url

from news.views.admin import NewsAdminAPI

urlpatterns = [
    url(r"^news/?$", NewsAdminAPI.as_view(), name="news_admin_api"),

]