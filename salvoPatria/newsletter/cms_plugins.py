from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from models import Newsletter

class Newsletter(CMSPluginBase):
    model = Newsletter
    name = _("Newsletter")
    render_template = "newsletter.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(Newsletter)