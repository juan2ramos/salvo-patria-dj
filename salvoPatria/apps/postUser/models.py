from django.db import models

class Post(models.Model):
	title 	= models.CharField(max_length=200)
	post  	= models.TextField(max_length=300)
	status 	= models.BooleanField(default=True)
	def __unicode__	(self):
		return self.title
