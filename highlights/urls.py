from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'highlights.views.home', name='home'),
    # url(r'^highlights/', include('highlights.foo.urls')),
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', 'posts.views.logout_view'),
    (r'^$', 'posts.views.index'),
    (r'^search/(?P<hashtag>\w+)/$', 'posts.views.hashtag_highlights'),
    (r'^emotion/(?P<emotion>\w+)/$', 'posts.views.highlights_emotions'),
    (r'^bigness/(?P<bigness>\w+)/$', 'posts.views.highlights_bigness'),
    (r'^public-feed/$', 'posts.views.highlights_public'),
    (r'^add-highlight/$', 'posts.views.add_highlight'),
    (r'^dashboard/$', 'posts.views.highlights_dashboard'),
    (r'^settings/$', 'posts.views.user_settings'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
