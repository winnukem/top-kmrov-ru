from django.conf.urls.defaults import *

import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$',                     'top.views.index'),
    (r'^nofilters/$',            'top.views.nofilters'),
    
    (r'^openid/', include('django_openidconsumer.urls')),

    (r'^exclude-author/',             'top.views.exclude_author'),
    (r'^return-author/',             'top.views.return_author'),
    (r'^exclude-post/',               'top.views.exclude_post'),
    (r'^return-post/',               'top.views.return_post'),
    (r'^settings/',                   'top.views.settings'),
    # Example:
    # (r'^top_webapp/', include('top_webapp.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
           (r'^static/(?P<path>.*)$', 'django.views.static.serve', 
                                         {'document_root': settings.MEDIA_ROOT,}),
           )

