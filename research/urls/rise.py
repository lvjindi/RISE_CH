from django.conf.urls import url

from research.views.rise import IntroductionAPI, PublicationAPI, ReportAPI, ProjectListAPI, ProjectDetailAPI

urlpatterns = [
    url(r"^introduction", IntroductionAPI.as_view(), name="introduction_api"),
    url(r"^project/list/?$", ProjectListAPI.as_view(), name="project_list_api"),
    url(r"^project/detail/?$", ProjectDetailAPI.as_view(), name="project_detail_api"),
    url(r"^publication", PublicationAPI.as_view(), name="publication_api"),
    url(r"^report", ReportAPI.as_view(), name="report_api"),
]
