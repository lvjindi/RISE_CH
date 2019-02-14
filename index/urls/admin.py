
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from index.views.admin import SlideAdminAPI, DrMessageAdminAPI, IndexAdminAPI

urlpatterns = [
    url(r"^index/slider/?$", SlideAdminAPI.as_view(), name='slider_admin_api'),
    url(r"^index/message/?$", DrMessageAdminAPI.as_view(), name="message_from_dr_admin_api"),
    url(r"^index/?$", IndexAdminAPI.as_view(), name="index_admin_api"),

]

urlpatterns += staticfiles_urlpatterns()