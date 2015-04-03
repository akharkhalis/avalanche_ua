# -*- coding: utf-8 -*-

from django.db import models

class triger(models.Model):
    """direction Model"""
    class Meta(object):
        verbose_name = u"Причина"
    triger = models.CharField(
        max_length=20,
        blank=False,
        verbose_name=u"напрям")
    def __unicode__(self):
        return u"%s" % (self.triger)