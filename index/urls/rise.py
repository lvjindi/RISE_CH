
from django.conf.urls import url

from index.views.rise import SliderImageAPI, MessageFromDrAPI

urlpatterns = [
    url(r"^index/slider/?$", SliderImageAPI.as_view(), name="slider_image_api"),
    url(r"^index/message/?$", MessageFromDrAPI.as_view(), name="message_from_dr_api"),

]