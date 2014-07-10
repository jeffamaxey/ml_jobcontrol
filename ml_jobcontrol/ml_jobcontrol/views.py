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
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view

# Local imports
from .permissions import IsOwnerOrReadOnly

from .models import MLModel
from .models import MLDataSet
from .models import MLModelConfig
from .models import MLClassificationTestSet

from .serializers import UserSerializer
from .serializers import MLModelSerializer
from .serializers import MLDataSetSerializer
from .serializers import MLModelConfigSerializer
from .serializers import MLClassificationTestSetSerializer

logger = logging.getLogger(__name__)


class MLDataSetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = MLDataSet.objects.all()
    serializer_class = MLDataSetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class MLClassificationTestSetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = MLClassificationTestSet.objects.all()
    serializer_class = MLClassificationTestSetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class MLModelViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = MLModel.objects.all()
    serializer_class = MLModelSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class MLModelConfigViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = MLModelConfig.objects.all()
    serializer_class = MLModelConfigSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
