from django.conf.urls import url
from django.views.static import serve

from Rise_CH.settings import MEDIA_ROOT

urlpatterns = [
    # 处理 media 信息，用于图片获取
    url(r'^static/media/(?P<path>.*)$', serve, {"document_root":MEDIA_ROOT}),
]