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


class MLDataSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLDataSet
        fields = ('id', 'name', 'url')

    def pre_save(self, obj):
        obj.owner = self.request.user


class UserSerializer(serializers.ModelSerializer):
    mldatasets = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'mldatasets')
