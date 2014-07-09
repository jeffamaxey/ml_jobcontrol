# -*- encoding: utf-8 -*-
# Standard library imports
from __future__ import absolute_import
import logging

# Imports from core django
from django.http import Http404
from django.contrib.auth.models import User

# Imports from third party apps
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view

# Local imports
from .models import MLDataSet
from .serializers import UserSerializer
from .serializers import MLDataSetSerializer
from .permissions import IsOwnerOrReadOnly

logger = logging.getLogger(__name__)

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'mldatasets': reverse('mldataset-list', request=request, format=format)
    })


class MLDataSetList(generics.ListCreateAPIView):
    """
    List all MLDataSets, or create a new mldataset.
    """
    queryset = MLDataSet.objects.all()
    serializer_class = MLDataSetSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class MLDataSetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MLDataSet.objects.all()
    serializer_class = MLDataSetSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
