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
from rest_framework.urlpatterns import format_suffix_patterns

# Local imports
from . import views

logger = logging.getLogger(__name__)

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

mldatasets_list = views.MLDataSetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
mldatasets_detail = views.MLDataSetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
user_list = views.UserViewSet.as_view({
    'get': 'list'
})
user_detail = views.UserViewSet.as_view({
    'get': 'retrieve'
})


urlpatterns = patterns('',
    #url(r'^$', TemplateView.as_view(template_name='base.html')),

    # Examples:
    # url(r'^$', 'ml_jobcontrol.views.home', name='home'),
    # url(r'^ml_jobcontrol/', include('ml_jobcontrol.foo.urls')),
    url(r'^mldatasets/$', mldatasets_list, name='mldataset-list'),
    url(r'^mldatasets/(?P<pk>[0-9]+)/$', mldatasets_detail,
        name='mldatasets-detail'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
    url(r'^$', views.api_root, name='api-root'),

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
