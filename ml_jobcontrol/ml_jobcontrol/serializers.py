# -*- encoding: utf-8 -*-
# Standard library imports
from __future__ import absolute_import
import logging

# Imports from core django

# Imports from third party apps
from rest_framework import serializers

# Local imports
from .models import MLDataSet

logger = logging.getLogger(__name__)


class MLDataSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLDataSet
        fields = ('id', 'name', 'url')
