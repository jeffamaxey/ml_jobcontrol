# -*- encoding: utf-8 -*-
# Standard library imports
from __future__ import absolute_import
import logging

# Imports from core django
from django.contrib.auth.models import User

# Imports from third party apps
from rest_framework import serializers

# Local imports
from .models import MLModel
from .models import MLDataSet
from .models import MLModelConfig
from .models import MLClassificationTestSet

logger = logging.getLogger(__name__)


class MLDataSetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')
    mlclassificationtestsets = serializers.HyperlinkedRelatedField(many=True,
        view_name='mlclassificationtestset-detail')

    class Meta:
        model = MLDataSet
        fields = ('id', 'name', 'url', 'owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    mldatasets = serializers.HyperlinkedRelatedField(many=True,
        view_name='mldataset-detail')

    class Meta:
        model = User
        fields = ('id', 'username', 'mldatasets')


class MLClassificationTestSetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')
    mldataset = serializers.HyperlinkedRelatedField(
        view_name="mldataset-detail")

    class Meta:
        model = MLClassificationTestSet
        fields = ('id', 'train_num', 'test_num', 'mldataset', 'owner')


class MLModelSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')
    mlmodelconfigs = serializers.HyperlinkedRelatedField(many=True,
        view_name='modelconfig-detail')

    class Meta:
        model = MLModel
        fields = ('id', 'name', 'import_path', 'mlmodelconfigs', 'owner')


class MLModelConfigSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MLModelConfig
        fields = ('id', 'created', 'json_config', 'mlmodel')
