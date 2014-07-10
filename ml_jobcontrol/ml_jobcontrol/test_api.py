# -*- encoding: utf-8 -*-
# Standard library imports
from __future__ import absolute_import
import json
import logging
from pprint import pprint
from pprint import pformat
from datetime import datetime, timedelta

# Imports from core django
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test.client import RequestFactory

# Imports from third party apps
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

# Local imports
from .models import MLModel
from .models import MLScore
from .models import MLDataSet
from .models import MLModelConfig
from .models import MLClassificationTestSet
from .views import MLScoreViewSet

logger = logging.getLogger(__name__)

class RestApiBaseTests(APITestCase):
    def setUp(self):
        MLScore.objects.get_or_create(name="foobar")
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            username='foo', email='foo@…', password='secret')
        MLDataSet.objects.get_or_create(name="foobar",
            url="http://example.org", owner=self.user)

    def test_scores_list(self):
        """
        Just test wether a setUp created score got into db.
        """
        url = reverse("mlscore-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content)
        self.assertEqual(len(data), 1)

    def test_create_mlmodel(self):
        """
        Ensure we can create a new mlmodel object.
        """
        url = reverse('mlmodel-list')
        data = {'name': 'foobar', 'import_path': 'classifiers.Foo'}
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format='json')
        rdata = {k: v for k, v in response.data.iteritems()
            if k in ("name", "import_path")}
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(rdata, data)

    def test_create_mlscore(self):
        """
        Test with request factory instead of api client.
        """
        data = {'name': 'asdf'}
        url = reverse("mlscore-list")
        request = self.factory.post(url, data, format='json')
        request.user = self.user
        force_authenticate(request, user=self.user)
        view = MLScoreViewSet.as_view({'post': 'create'})
        response = view(request)
        rdata = {k: v for k, v in response.data.iteritems()
            if k in ("name",)}
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(rdata, data)

    def test_mldataset_list(self):
        """
        Just test wether a setUp created mldataset got into db.
        """
        url = reverse("mldataset-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content)
        self.assertEqual(len(data), 1)

    def test_only_owner_delete_mldataset(self):
        """
        Ensure only the owner has the permission to delete a mldataset.
        """
        mld = MLDataSet.objects.all()[0]
        url = reverse('mldataset-detail', kwargs={'pk': mld.pk})
        tmp_user = User(username="foobar", password='foobar')
        self.client.force_authenticate(user=tmp_user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_owner_delete_mldataset(self):
        """
        Ensure the owner has the permission to delete a mldataset.
        """
        mld = MLDataSet.objects.all()[0]
        url = reverse('mldataset-detail', kwargs={'pk': mld.pk})
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class RestApiUseCaseTests(APITestCase):
    def setUp(self):
        self.mlscores = []
        mlscore, created = MLScore.objects.get_or_create(name="precision")
        self.mlscores.append(mlscore)
        mlscore, created = MLScore.objects.get_or_create(name="recall")
        self.mlscores.append(mlscore)
        self.user = User.objects.create_user(
            username='foo', email='foo@…', password='secret')
        mldataset, created = MLDataSet.objects.get_or_create(
            name="foo dataset", url="http://example.org", owner=self.user)
        mlmodel, created = MLModel.objects.get_or_create(name="foo model",
            import_path="classifiers.Foo", owner=self.user)
        self.mlconfig, created = MLModelConfig.objects.get_or_create(
            mlmodel=mlmodel, json_config='{"asdf":"bsdf"}')
        self.mltestset, created = \
            MLClassificationTestSet.objects.get_or_create(
                mldataset=mldataset, train_num=1000, test_num=300,
                owner=self.user)

    def test_submit_result(self):
        """
        Submit complete precision/recall test result for known
        model config + classification testset.
        """
        mlresult_url = reverse("mlresult-list")
        self.client.force_authenticate(user=self.user)
        mlconfig_url = reverse("mlmodelconfig-detail",
            kwargs={"pk": self.mlconfig.pk})
        mltestset_url = reverse("mlclassificationtestset-detail",
            kwargs={"pk": self.mltestset.pk})
        mlscore_urls = [reverse("mlscore-detail",
            kwargs={"pk": mlscore.pk}) for mlscore in self.mlscores]
        pprint(mlscore_urls)
        data = {
            "mlmodel_config": mlconfig_url,
            "mlclassification_testset": mltestset_url,
        }
        response = self.client.post(mlresult_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        new_mlresult_url = reverse("mlresult-detail",
            kwargs={"pk": response.data["id"]})
        mlresultscore_url = reverse("mlresultscore-list")
        for num, mlscore_url in enumerate(mlscore_urls):
            data = {
                "mlresult": new_mlresult_url,
                "mlscore": mlscore_url,
                "score": 1.0 / float(num + 1),
            }
            response = self.client.post(mlresultscore_url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
