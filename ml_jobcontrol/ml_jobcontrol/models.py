# -*- encoding: utf-8 -*-
# Standard library imports
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
    owner = models.ForeignKey('auth.User', related_name='mldatasets',
        null=True, default=None)


class MLClassificationTestSet(TimeStampedModel):
    mldataset = models.ForeignKey(MLDataSet)
    train_num = models.IntegerField()
    test_num = models.IntegerField()
    owner = models.ForeignKey('auth.User',
        related_name='mlclassificationtestsets', null=True, default=None)


class MLModel(TimeStampedModel):
    name = models.CharField(max_length=100)
    import_path = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey('auth.User', related_name='mlmodels',
        null=True, default=None)


class MLModelConfig(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    mlmodel = models.ForeignKey(MLModel, related_name='mlmodelconfigs')
    json_config  = models.TextField(unique=True)


class MLScore(TimeStampedModel):
    name = models.CharField(max_length=100)


class MLJob(TimeStampedModel):
    mlmodel_config = models.ForeignKey(MLModelConfig)
    mlclassification_testset = models.ForeignKey(MLClassificationTestSet)


class MLResult(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    mljob = models.ForeignKey(MLJob)
    scores = models.ManyToManyField(MLScore, through='MLResultScore')


class MLResultScore(models.Model):
    mlresult = models.ForeignKey(MLResult)
    mlscore = models.ForeignKey(MLScore)    
    score = models.FloatField()
