# -*- coding: utf-8 -*-
from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class DisqusService(models.Model):
    shortname = models.CharField(
        verbose_name=_('Shortname'),
        unique=True,
        blank=True,
        max_length=100
    )

    def __str__(self):
        return '{}'.format(self.shortname)

class DisqusPlugin(CMSPlugin):
    disqus = models.ForeignKey(
        DisqusService,
        verbose_name=_('Disqus Service'),
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    def __str__(self):
        return '{}'.format(self.disqus)

    def copy_relations(self, old_instance):
        self.disqus = old_instance.disqus
