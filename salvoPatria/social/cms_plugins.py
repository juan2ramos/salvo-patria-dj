from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from twython import Twython
from models import Social

class Social(CMSPluginBase):
    model = Social
    name = _("Social")
    render_template = "social.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(Social)