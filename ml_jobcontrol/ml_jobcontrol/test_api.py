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

# Imports from third party apps
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

# Local imports

logger = logging.getLogger(__name__)

class MLModelTests(APITestCase):
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
