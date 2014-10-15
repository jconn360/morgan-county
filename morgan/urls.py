from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
    url(r'^api/1.0/', include('morgan.api.v1.urls')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    # url('', include('morgan.apps.')),
)
