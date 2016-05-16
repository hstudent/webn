"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
import django.views.defaults

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^question/', include('qa.urls')),
    url(r'^question/(\d+)/$', 'qa.views.test'),
    url(r'^login/',  django.views.defaults.page_not_found, {'exception':''}),
    url(r'^signup/',  django.views.defaults.page_not_found, {'exception':''}),
    url(r'^ask/', django.views.defaults.page_not_found, {'exception':''}),
    url(r'popular/',  django.views.defaults.page_not_found, {'exception':''}),
    url(r'new/', django.views.defaults.page_not_found, {'exception':''}),
]
