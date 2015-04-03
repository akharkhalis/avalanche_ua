# -*- coding: utf-8 -*-

from django.db import models

class locations(models.Model):
    """locations Model"""
    class Meta(object):
        verbose_name = u"Локація"
        verbose_name_plural = u"Локації"
    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Назва")
    location_coor_x = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"X")
    location_coor_y = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Y")    
    notes = models.TextField(
        blank=True,
        verbose_name=u"Додаткові нотатки")
    def __unicode__(self):
        return u"%s" % (self.title)