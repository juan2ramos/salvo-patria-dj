# -*- coding: utf-8 -*-
from cms.models.pluginmodel import CMSPlugin

from django.db import models

class Social(CMSPlugin):
    title = models.CharField(max_length=255, default='tit')
    subtitle = models.TextField(default='')
