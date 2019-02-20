from django.conf.urls import url
from patterns import patterns

from controller.views import get_ueditor_controller

urlpatterns = [
    url(r'^controller/$', get_ueditor_controller, name='get_ueditor_controller')
]
