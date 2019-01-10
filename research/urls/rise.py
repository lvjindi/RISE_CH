from django.conf.urls import url

from research.views.rise import IntroductionAPI, ProjectAPI, PublicationAPI, ReportAPI

urlpatterns = [
    url(r"^introduction", IntroductionAPI.as_view(), name="introduction_api"),
    url(r"^project", ProjectAPI.as_view(), name="project_api"),
    url(r"^publication", PublicationAPI.as_view(), name="publication_api"),
    url(r"^report", ReportAPI.as_view(), name="report_api"),
]