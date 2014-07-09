# -*- encoding: utf-8 -*-
# Standard library imports
from __future__ import absolute_import
import logging

# Imports from core django
from django.http import Http404

# Imports from third party apps
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Local imports
from .models import MLDataSet
from .serializers import MLDataSetSerializer

logger = logging.getLogger(__name__)


class MLDataSetList(APIView):
    """
    List all MLDataSets, or create a new mldataset.
    """
    def get(self, request, format=None):
        mldatasets = MLDataSet.objects.all()
        serializer = MLDataSetSerializer(mldatasets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MLDataSetSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
