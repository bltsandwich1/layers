from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'layers.profiles.views.home', name='home'),
     url(r'^my_account/', 'layers.profiles.views.my_account', name='my_account'),
     url(r'get_started/', 'layers.get_started.views.get_started', name='get_started'),
     url(r'submit_design/', 'layers.get_started.views.submit_design', name='submit_design'),
     url(r'^complete_signup/$', 'layers.profiles.views.complete_signup', name='complete_signup'),
	 url(r'^my_account/$', 'layers.profiles.views.my_account', name='my_account'),    
     url(r'^logout/$', 'layers.profiles.views.logout_view', name='logout'),
     url(r'^login$', 'layers.landing.views.login_view', name='login'),
     url(r'^update_settings$', 'layers.profiles.views.update_settings', name='update_settings'),
     url(r'^add_project$', 'layers.projects.views.add_project', name='add_project'),
     url(r'^add_photo$', 'layers.projects.views.add_photo_to_project', name='add_photo'),
     url(r'^signup$', 'layers.landing.views.signup_view', name='signup'),
     url(r'^faq$', 'layers.landing.views.faq', name='faq'),
     url(r'^blog$', 'layers.landing.views.blog', name='blog'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
