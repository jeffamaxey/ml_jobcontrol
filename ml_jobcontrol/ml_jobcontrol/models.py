# -*- encoding: utf-8 -*-
# Standard library imports
from __future__ import absolute_import
import logging

# Imports from core django
from django.db import models

# Imports from third party apps

from model_utils.models import TimeStampedModel

# Local imports

logger = logging.getLogger(__name__)


class MLDataSet(TimeStampedModel):
    name = models.CharField(max_length=100)
    url = models.URLField(unique=True)
    owner = models.ForeignKey('auth.User', related_name='mldatasets', null=True, default=None)


class MLClassificationTestSet(TimeStampedModel):
    mldataset = models.ForeignKey(MLDataSet)
    train_num = models.IntegerField()
    test_num = models.IntegerField()


class MLModel(TimeStampedModel):
    name = models.CharField(max_length=100)
    import_path = models.CharField(max_length=100, unique=True)


class MLModelConfig(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    mlmodel = models.ForeignKey(MLModel)
    json_config  = models.TextField(unique=True)


class MLScore(TimeStampedModel):
    name = models.CharField(max_length=100)


class MLResult(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    mlmodel_config = models.ForeignKey(MLModelConfig)
    mlclassification_testset = models.ForeignKey(MLClassificationTestSet)
    scores = models.ManyToManyField(MLScore, through='MLResultScore')


class MLResultScore(models.Model):
    mlresult = models.ForeignKey(MLResult)
    mlscore = models.ForeignKey(MLScore)    
    score = models.FloatField()
