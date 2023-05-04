# -*- encoding: utf-8 -*-
# Standard library imports
import logging

# Imports from core django
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Imports from third party apps
from rest_framework.routers import DefaultRouter

# Local imports
from . import views

logger = logging.getLogger(__name__)

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

router = DefaultRouter()
router.register(r'mldatasets', views.MLDataSetViewSet)
router.register(r'mlclassificationtestsets',
    views.MLClassificationTestSetViewSet)
router.register(r'mlmodels', views.MLModelViewSet)
router.register(r'mlmodelconfigs', views.MLModelConfigViewSet)
router.register(r'mljobs', views.MLJobViewSet)
router.register(r'mlresultscores', views.MLResultScoreViewSet)
router.register(r'mlscore', views.MLScoreViewSet)
router.register(r'users', views.UserViewSet)
API_PREFIX = "api/v1"

urlpatterns = patterns('', url(f'^{API_PREFIX}/', include(router.urls)))

# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )

# DRF authentication
urlpatterns += patterns(
    '',
    url(
        f'^{API_PREFIX}/api-auth/',
        include('rest_framework.urls', namespace='rest_framework'),
    ),
)
