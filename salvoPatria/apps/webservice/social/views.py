from django.http import HttpResponse
from twython import Twython
from apps.postUser.models import Post 
#	serializacion 
from django.core import serializers

def wsPost_view (request):
	data = serializers.serialize("json",Post.objects.filter(status=True))
	return HttpResponse(data,mimetype='application/json')
	# Create your views here.

def wsTwitter_view(request):
	APP_KEY = 'IfZu2KyFrUENObWRRb4rEQ'
	APP_SECRET = 'ZOw3Y9BoMpiZaaoqaL1OH3tH3BNHr2YoBQ4IF2JYu4s'
	OAUTH_TOKEN = '56143706-DqNvSdocUyKQsSkk6vweW66vtv9ovSfRDECmfzdk'
	OAUTH_TOKEN_SECRET = 'xZ6sIyxeoKcxcV5OchdjTDXJLXhnzrfu6zf6bUzJg7c'
	twitter = Twython(APP_KEY, APP_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
	tweets = twitter.get_home_timeline()
	return HttpResponse(tweets,mimetype='application/json')

