from django.conf.urls import url

from news.views.rise import NewsListAPI, NewsLatestListAPI, NewsDetailAPI, ImportantNewsListAPI

urlpatterns = [
    url(r"^news/list/?$", NewsListAPI.as_view(), name="news_list_api"),
    url(r"^news/list/latest?$", NewsLatestListAPI.as_view(), name="news_latest_list_api"),
    url(r"^news/list/important?$", ImportantNewsListAPI.as_view(), name="news_important_list_api"),
    url(r"^news/detail/?$", NewsDetailAPI.as_view(), name="news_detail_api"),

]
