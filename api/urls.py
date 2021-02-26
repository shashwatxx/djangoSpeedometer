from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from api import views

from django.views.generic.base import RedirectView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'rspeed', views.ReadSpeedViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
   
]
