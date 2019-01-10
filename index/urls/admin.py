from django.conf.urls import url

from index.views.admin import SlideAdminAPI, DrMessageAdminAPI

urlpatterns = [
    url(r"^index/slider/?$", SlideAdminAPI.as_view(), name='slider_admin_api'),
    url(r"^index/message/?$", DrMessageAdminAPI.as_view(), name="message_from_dr_admin_api")
]
