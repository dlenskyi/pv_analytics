from django.contrib import admin
from django.views.i18n import set_language
from django.views.static import serve
from django.urls import path, include, re_path

from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings

admin.autodiscover()

urlpatterns = [
    path('i18n/setlang/', set_language, name='set-language'),
    re_path(r'^i18n/', include('django.conf.urls.i18n')),
    # URLs that do not require a session or valid token
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    re_path(
        r'^static/(?P<path>.*)$',
        serve,
        {'document_root': settings.STATIC_ROOT},
    ),
    re_path(
        r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}
    ),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += [
    path(
        'api/v1/',
        include(('pv_analytics.api.v1.urls', 'api'), namespace='api_v1'),
    ),
]

urlpatterns += [
    path('admin/', admin.site.urls, name='admin-page'),
]

if settings.DEBUG and (settings.SERVER_TYPE not in ['PRODUCTION', 'STAGING']):
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

urlpatterns += [
    path('', include('pv_analytics.apps.front.urls')),
]
