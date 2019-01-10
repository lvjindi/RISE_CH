from django.conf.urls import url

from seminars.views.admin import SeminarAdminAPI

urlpatterns = [
    url(r"^seminar?$", SeminarAdminAPI.as_view(), name="seminar_admin_api"),


]