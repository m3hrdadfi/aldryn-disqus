# -*- coding: utf-8 -*-
from aldryn_disqus import models
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class DisqusPlugin(CMSPluginBase):
    model = models.DisqusPlugin
    name = _('Disqus Plugin')
    render_template = 'aldryn_disqus/disqus.html'
    admin_preview = False
    page_only = True
    allow_children = True

    def render(self, context, instance, placeholder):
        context['DISQUS_SHORTNAME'] = instance.disqus.shortname if instance and instance.disqus and \
                                                                   instance.disqus.shortname else None
        context['instance'] = instance
        context['developer_mode'] = settings.DEBUG
        return context


plugin_pool.register_plugin(DisqusPlugin)
