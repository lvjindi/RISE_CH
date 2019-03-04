from django.conf.urls import url

from aboutUs.views.rise import AboutUsDetailAPI

urlpatterns = [
    url(r"^aboutUs/?$", AboutUsDetailAPI.as_view(), name="aboutUs_detail_list_api"),


]