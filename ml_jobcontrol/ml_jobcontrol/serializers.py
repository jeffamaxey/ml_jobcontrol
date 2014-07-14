# -*- encoding: utf-8 -*-
# Standard library imports
import logging
from pprint import pformat

# Imports from core django
from django.contrib.auth.models import User

# Imports from third party apps
from rest_framework import serializers

# Local imports
from .models import MLJob
from .models import MLModel
from .models import MLScore
from .models import MLDataSet
from .models import MLModelConfig
from .models import MLResultScore
from .models import MLClassificationTestSet

logger = logging.getLogger(__name__)


class MLDataSetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')
    mlclassificationtestsets = serializers.HyperlinkedRelatedField(many=True,
        view_name='mlclassificationtestset-detail')

    class Meta:
        model = MLDataSet
        fields = ('id', 'name', 'url', 'owner')


class MLDataSetJobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MLDataSet
        fields = ('url', 'name', 'url')


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


class MLClassificationTestSetJobSerializer(serializers.HyperlinkedModelSerializer):
    mldataset = MLDataSetJobSerializer()

    class Meta:
        model = MLClassificationTestSet
        fields = ('url', 'train_num', 'test_num', 'mldataset')


class MLModelSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')

    class Meta:
        model = MLModel
        fields = ('id', 'name', 'import_path', 'mlmodelconfigs', 'owner')


class MLModelJobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MLModel
        fields = ('name', 'import_path')


class MLModelConfigSerializer(serializers.HyperlinkedModelSerializer):
    mlmodel = serializers.HyperlinkedRelatedField(
        view_name='mlmodel-detail')

    class Meta:
        model = MLModelConfig
        fields = ('id', 'created', 'json_config', 'mlmodel')


class MLModelConfigJobSerializer(serializers.HyperlinkedModelSerializer):
    mlmodel = MLModelJobSerializer()

    class Meta:
        model = MLModelConfig
        fields = ('url', 'json_config', 'mlmodel')


class MLResultScoreSerializer(serializers.HyperlinkedModelSerializer):
    mljob = serializers.HyperlinkedRelatedField(
        view_name='mljob-detail')
    mlscore = serializers.HyperlinkedRelatedField(
        view_name='mlscore-detail')

    class Meta:
        model = MLResultScore
        fields = ('id', 'mljob', 'mlscore', "score")


class MLScoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MLScore
        fields = ('id', 'name')


class MLJobSerializer(serializers.HyperlinkedModelSerializer):
    mlmodel_config = serializers.HyperlinkedRelatedField(
        view_name='mlmodelconfig-detail')
    mlclassification_testset = serializers.HyperlinkedRelatedField(
        view_name='mlclassificationtestset-detail')
    model_config = MLModelConfigJobSerializer(source='mlmodel_config',
        required=False, read_only=True)
    classification_testset = MLClassificationTestSetJobSerializer(
        source='mlclassification_testset', read_only=True)
    scores = serializers.HyperlinkedRelatedField(many=True,
        view_name='mlresultscore-detail', read_only=True)

    class Meta:
        model = MLJob
        fields = ('url', 'created', 'status', 'scores', 'model_config',
            'classification_testset', 'mlmodel_config',
            'mlclassification_testset')
