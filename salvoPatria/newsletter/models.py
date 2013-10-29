# -*- coding: utf-8 -*-
from cms.models.pluginmodel import CMSPlugin

from django.db import models

class Newsletter(CMSPlugin):
    title = models.CharField(max_length=255, default='Nuestro newsletter, pensado para usted')
    subtitle = models.TextField(default='Un newsletter pensado para usted: casos de éxito, comentarios y reflexiones acerca de la gestión de proyectos. Nunca spam.')
