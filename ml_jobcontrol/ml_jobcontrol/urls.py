# -*- encoding: utf-8 -*-
# Standard library imports
from __future__ import absolute_import
import logging

# Imports from core django
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

# Imports from third party apps
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

# Local imports
from . import views

logger = logging.getLogger(__name__)

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

router = DefaultRouter()
router.register(r'mldatasets', views.MLDataSetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = patterns('',
    #url(r'^$', TemplateView.as_view(template_name='base.html')),

    # Examples:
    # url(r'^$', 'ml_jobcontrol.views.home', name='home'),
    url(r'^', include(router.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    
)

# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )

# DRF authentication
urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)
