from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from index.views.admin import SlideAdminAPI, DrMessageAdminAPI, IndexAdminAPI, SliderAdminAPI, MessageAdminAPI, \
    SliderPublicAdminAPI, MessagePublicAdminAPI

urlpatterns = [
    url(r"^index/slider/?$", SlideAdminAPI.as_view(), name='slider_admin_api'),
    url(r"^index/message/?$", DrMessageAdminAPI.as_view(), name="message_from_dr_admin_api"),
    url(r"^index/?$", IndexAdminAPI.as_view(), name="index_admin_api"),
    url(r"^index/slider_management/?$", SliderAdminAPI.as_view(), name="index_slider_api"),
    url(r"^index/slider_public/?$", SliderPublicAdminAPI.as_view(), name="index_slider_public_api"),
    url(r"^index/message_management/?$", MessageAdminAPI.as_view(), name="index_message_api"),
    url(r"^index/message_public/?$", MessagePublicAdminAPI.as_view(), name="index_message_public_api"),

]

urlpatterns += staticfiles_urlpatterns()
