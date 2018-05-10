#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
import views

urlpatterns = [

	url(r'^fake_query/$', views.fake_query),

]

