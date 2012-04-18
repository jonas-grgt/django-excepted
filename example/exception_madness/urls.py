from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
        (r'', 'exception_madness.views.will_throw_exception'),
)
