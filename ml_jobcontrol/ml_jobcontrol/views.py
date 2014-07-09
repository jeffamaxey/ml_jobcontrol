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

# Local imports
from .models import MLDataSet
from .serializers import UserSerializer
from .serializers import MLDataSetSerializer

logger = logging.getLogger(__name__)


class MLDataSetList(generics.ListCreateAPIView):
    """
    List all MLDataSets, or create a new mldataset.
    """
    queryset = MLDataSet.objects.all()
    serializer_class = MLDataSetSerializer


class MLDataSetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MLDataSet.objects.all()
    serializer_class = MLDataSetSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
