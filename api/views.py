from django.shortcuts import render
from django.views.generic.edit import CreateView

from api.models import ReadSpeed
from django.urls.base import reverse_lazy, reverse
from django.http import HttpResponsePermanentRedirect
from api import ML
from rest_framework import viewsets
from rest_framework.response import Response
from api.serializers import ReadSpeedSerializer


class ReadSpeedViewSet(viewsets.ModelViewSet):
    queryset = ReadSpeed.objects.all().order_by('-id')
    serializer_class = ReadSpeedSerializer
    def create(self, request, *args, **kwargs):
        super(viewsets.ModelViewSet, self).create(request, *args, **kwargs)
        ob = ReadSpeed.objects.latest('id')
        # print("*"*100)
        # print(pk)
        # ob = ReadSpeed.objects.get(pk=pk)
        y = ML.pred(ob)
        return Response({"status": "Success", "Hours": y})  # Your override
