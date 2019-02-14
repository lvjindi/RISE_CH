from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from research.views.admin import ResearchAdminAPI, ProjectAdminAPI, PublicationAdminAPI, ReportAdminAPI, \
    ResearchManageAdminAPI

urlpatterns = [
    url(r"^introduction/", ResearchAdminAPI.as_view(), name="research_admin_api"),
    url(r"^project/", ProjectAdminAPI.as_view(), name="project_admin_api"),
    url(r"^publication/", PublicationAdminAPI.as_view(), name="publication_admin_api"),
    url(r"^report/", ReportAdminAPI.as_view(), name="report_admin_api"),
    url(r"^research_management/", ResearchManageAdminAPI.as_view(), name="report_management_admin_api")
]
urlpatterns += staticfiles_urlpatterns()
