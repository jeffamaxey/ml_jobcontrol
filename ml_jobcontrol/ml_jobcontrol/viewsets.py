# -*- encoding: utf-8 -*-
# Standard library imports
from __future__ import absolute_import
import logging

# Imports from core django

# Imports from third party apps
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework_bulk.mixins import BulkCreateModelMixin

# Local imports

class BulkCreateViewSet(BulkCreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    pass
