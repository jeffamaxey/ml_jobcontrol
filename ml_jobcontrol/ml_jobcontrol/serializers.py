# -*- encoding: utf-8 -*-
# Standard library imports
from __future__ import absolute_import
import logging

# Imports from core django
from django.contrib.auth.models import User

# Imports from third party apps
from rest_framework import serializers

# Local imports
from .models import MLDataSet

logger = logging.getLogger(__name__)


class MLDataSetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')

    class Meta:
        model = MLDataSet
        fields = ('id', 'name', 'url', 'owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    mldatasets = serializers.HyperlinkedRelatedField(many=True,
        view_name='mldatasets-detail')

    class Meta:
        model = User
        fields = ('id', 'username', 'mldatasets')
