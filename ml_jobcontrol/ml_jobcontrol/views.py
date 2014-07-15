# -*- encoding: utf-8 -*-
# Standard library imports
import logging
from pprint import pformat, pprint

# Imports from core django
from django.contrib.auth.models import User

# Imports from third party apps
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.exceptions import APIException

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
    queryset = MLDataSet.objects.all()
    serializer_class = MLDataSetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class MLClassificationTestSetViewSet(viewsets.ModelViewSet):
    queryset = MLClassificationTestSet.objects.all()
    serializer_class = MLClassificationTestSetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class MLModelViewSet(viewsets.ModelViewSet):
    queryset = MLModel.objects.all()
    serializer_class = MLModelSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class MLModelConfigViewSet(viewsets.ModelViewSet):
    queryset = MLModelConfig.objects.all()
    serializer_class = MLModelConfigSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


#class MLResultScoreViewSet(viewsets.ModelViewSet):
class MLResultScoreViewSet(BulkCreateViewSet):
    queryset = MLResultScore.objects.all()
    serializer_class = MLResultScoreSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class MLScoreViewSet(viewsets.ModelViewSet):
    queryset = MLScore.objects.all()
    serializer_class = MLScoreSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class StatusConflictException(APIException):
    status_code = 409

    def __init__(self, detail):
        self.detail = detail


class MLJobViewSet(viewsets.ModelViewSet):
    queryset = MLJob.objects.all()
    serializer_class = MLJobSerializer
    allowed_status_updates = {
        "todo": set(["in_progress", "done"]),
        "in_progress": set(["done"]),
        "done": set(),
    }

    def get_queryset(self):
        filtered_status = self.request.QUERY_PARAMS.get("status")
        if filtered_status is not None:
            return self.queryset.filter(status=filtered_status)
        return self.queryset

    def pre_save(self, obj):
        old_obj = self.get_object_or_none()
        if old_obj is not None:
            # old_obj does exist -> update status case
            # updates of config or testset are not permitted
            # delete old job and create new one
            if obj.status not in self.allowed_status_updates.get(
                old_obj.status, set()):
                raise StatusConflictException(
                    "can't change status from %s to %s" % (
                        old_obj.status, obj.status))


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
