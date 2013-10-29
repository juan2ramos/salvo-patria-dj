from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('apps.webservice.social.views',
		url(r'^ws/social/$', 'wsPost_view',name = "ws_Post_view_url"),
		url(r'^ws/tweets/$', 'wsTwitter_view',name = "ws_Twitter_view_url"),
	)
