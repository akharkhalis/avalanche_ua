# -*- coding: utf-8 -*-

from django.db import models

class direction(models.Model):
    """direction Model"""
    class Meta(object):
        verbose_name = u"Напрям"
    direction = models.CharField(
        max_length=2,
        blank=False,
        verbose_name=u"напрям")
    degrees = models.CharField(
        max_length=3,
        blank=False,
        verbose_name=u"Азимут")
    def __unicode__(self):
        return u"%s" % (self.direction)