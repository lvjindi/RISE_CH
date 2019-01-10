from django.conf.urls import url

from upload.views.admin import UploadAdminAPI

urlpatterns = [
    url(r"^upload/", UploadAdminAPI.as_view(), name="upload_admin_api"),

]
