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
from .models import MLScore
from .views import MLScoreViewSet

logger = logging.getLogger(__name__)

class RestApiTests(APITestCase):
    def setUp(self):
        MLScore.objects.get_or_create(name="foobar")
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            username='foo', email='foo@…', password='secret')

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
        tmp_user = User(username="foobar", password='foobar')
        self.client.force_authenticate(user=tmp_user)
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
        request = self.factory.post('/mlscore/1/', data, format='json')
        request.user = self.user
        force_authenticate(request, user=self.user)
        view = MLScoreViewSet.as_view({'post': 'create'})
        response = view(request)
        rdata = {k: v for k, v in response.data.iteritems()
            if k in ("name",)}
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(rdata, data)
