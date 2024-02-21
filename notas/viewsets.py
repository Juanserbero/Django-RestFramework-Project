from django.shortcuts import render,redirect,get_object_or_404
from notas.models import *
from notas.serilizers import *
from rest_framework import viewsets


class NotaViewsets(viewsets.ModelViewSet):
    queryset = Notas.objects.all()
    serializer_class = NotaSerializer