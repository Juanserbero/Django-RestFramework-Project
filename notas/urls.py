from django.urls import path, include
from notas import viewsets
from rest_framework import routers
from .viewsets import *


router = routers.DefaultRouter()
router.register(r'notas', NotaViewsets)


urlpatterns = router.urls
