import settings
#from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    #Admin and Media
    url#(r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
    (r'^static/(?P<path>.*)$', 'django.contrib.staticfiles.views.serve',
		 		 {'document_root': settings.STATIC_ROOT}),

    # Home Page
	(r'^$', 'classify.views.HomePage'),
	
	# Estimation
	(r'^estimate/$', 'classify.views.Estimation'),
	(r'^result/$', 'classify.views.Result'),
	  
)
