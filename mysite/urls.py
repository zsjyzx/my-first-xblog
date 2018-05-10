"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from views import RegisterView
from django.contrib.auth import views as auth_views
#from testdb import views as testdb_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # blog
    url(r'^blog/', include('blog.urls')),

    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url('', include('django.contrib.auth.urls')),
    #url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),

    # Test DB
    #url(r'^hello$', views.hello, name='hello'),
    #url(r'^testdb$', views.testdb, name='testdb'),

	# FAKE TEST
    url(r'^faketest/', include('mysite.faketest.urls')),

    # MDEDitor
    url(r'mdeditor/', include('mdeditor.urls')),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
