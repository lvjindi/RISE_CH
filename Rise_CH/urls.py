"""Rise_CH URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/admin/', include('account.urls')),
    path('api/', include('index.urls.rise')),
    path('api/admin/', include('index.urls.admin')),
    path('api/', include('people.urls.rise')),
    path('api/admin/', include('people.urls.admin')),
    path('api/', include('research.urls.rise')),
    path('api/admin/', include('research.urls.admin')),
    path('api/', include('seminars.urls.rise')),
    path('api/admin/', include('seminars.urls.admin')),
    path('api/', include('conference.urls.rise')),
    path('api/admin/', include('conference.urls.admin')),
    path('api/', include('exchanges.urls.rise')),
    path('api/admin/', include('exchanges.urls.admin')),
    path('api/', include('news.urls.rise')),
    path('api/admin/', include('news.urls.admin')),
    path('api/', include('join.urls.rise')),
    path('api/admin/', include('join.urls.admin')),
    path('api/admin/', include('upload.urls.admin')),
    path('api/', include('controller.urls')),
    path('api/', include('static.media.urls')),
    path('admin/', admin.site.urls)
]
