from django.db import models
from django_facebook.models import FacebookProfileModel

class MyCustomProfile(FacebookProfileModel):
    user = models.OneToOneField('auth.User')
