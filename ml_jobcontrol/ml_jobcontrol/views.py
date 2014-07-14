# -*- encoding: utf-8 -*-
# Standard library imports
import logging
from pprint import pformat

# Imports from core django
from django.contrib.auth.models import User

# Imports from third party apps
from rest_framework import viewsets
from rest_framework import permissions

# Local imports
from .permissions import IsOwnerOrReadOnly

from .models import MLJob
from .models import MLModel
from .models import MLScore
from .models import MLDataSet
from .models import MLModelConfig
from .models import MLResultScore
from .models import MLClassificationTestSet

from .serializers import UserSerializer
from .serializers import MLJobSerializer
from .serializers import MLModelSerializer
from .serializers import MLScoreSerializer
from .serializers import MLDataSetSerializer
from .serializers import MLModelConfigSerializer
from .serializers import MLResultScoreSerializer
from .serializers import MLClassificationTestSetSerializer

from .viewsets import BulkCreateViewSet

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


#class MLResultScoreViewSet(viewsets.ModelViewSet):
class MLResultScoreViewSet(BulkCreateViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = MLResultScore.objects.all()
    serializer_class = MLResultScoreSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class MLScoreViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = MLScore.objects.all()
    serializer_class = MLScoreSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class MLJobViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = MLJob.objects.all()
    serializer_class = MLJobSerializer

    def get_queryset(self):
        filtered_status = self.request.QUERY_PARAMS.get("status")
        if filtered_status is not None:
            return self.queryset.filter(status=filtered_status)
        return self.queryset


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
