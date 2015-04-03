# -*- coding: utf-8 -*-

from django.db import models

class aval_type(models.Model):
    """direction Model"""
    class Meta(object):
        verbose_name = u"Тип"
    type = models.CharField(
        max_length=20,
        blank=False,
        verbose_name=u"Тип")
    def __unicode__(self):
        return u"%s" % (self.type)