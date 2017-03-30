from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic.base import RedirectView

from django.conf.urls.static import static
from dv_apps.metrics import views_public_metrics
admin.site.site_header = 'Dataverse DB'

URL_PREFIX = 'miniverse/'


urlpatterns = [
    # Examples:
    # url(r'^$', 'miniverse.views.home', name='home'),
    url(r'^%sdr2m/' % URL_PREFIX, include('dv_apps.dvobjects.urls')),

    url(r'^%sdataset/' % URL_PREFIX, include('dv_apps.datasets.urls')),

    url(r'^%sdatafile/' % URL_PREFIX, include('dv_apps.datafiles.urls')),

    url(r'^%sdataverse/' % URL_PREFIX, include('dv_apps.dataverses.urls')),

    url(r'^%smap/' % URL_PREFIX, include('dv_apps.installations.urls')),

    url(r'^%smetrics/' % URL_PREFIX, include('dv_apps.metrics.urls')),

    url(r'^%sdvobjects/' % URL_PREFIX, include('dv_apps.dvobject_api.urls')),

    url(r'^%sqc/' % URL_PREFIX, include('dv_apps.quality_checks.urls')),

    url(r'^%sslackbot/' % URL_PREFIX, include('dv_apps.slackbot.urls')),

    url(r'^%sminiverse-admin/' % URL_PREFIX, include(admin.site.urls)),

    url(r'^%sminiverse-admin/' % URL_PREFIX, include(admin.site.urls)),

    url(r'^$', views_public_metrics.view_homepage_placeholder, name='view_homepage_placeholder'),

    url(r'^favicon.ico$', RedirectView.as_view(url='/static/favicondataverse.png', permanent=True), name='favicon')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^debug/', include(debug_toolbar.urls)),
    ]

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #urlpatterns += patterns('',
    #    url(r'^__debug__/', include(debug_toolbar.urls)),
    #)
