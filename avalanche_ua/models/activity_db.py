# -*- coding: utf-8 -*-

from django.db import models

class activity(models.Model):
    """Student Model"""

    class Meta(object):
        verbose_name = u"Лавина"
        verbose_name_plural = u"Лавини"

    date = models.DateField(
        blank=False,
        verbose_name=u"Дата",
        null=True)

    time = models.TimeField(
        blank=False,
        verbose_name=u"Час",
        null=True)

    coordinat x = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u"Довгота",
        default='')

    coordinat y = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u"Широта",
        default='')

    altitude = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u"Висота",
        default='')

    victims = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u"Потерпілі",
        default='')

    rel_volume = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u"Відноснийобєм",
        default='')


   # zone = models.ForeignKey('Group',
   #     verbose_name=u"Група",
   #     blank=False,
   #     null=True,
   #     on_delete=models.PROTECT)

    notes = models.TextField(
        blank=True,
        verbose_name=u"Додаткові нотатки")

    photo = models.ImageField(
        blank=True,
        verbose_name=u"Фото",
        null=True)

#observer data
    obs_first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Ім'я")
    obs_last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Прізвище")
    obs_phone = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Телефон")
    obs_mail = models.EmailField(
        max_length=256,
        blank=False,
        verbose_name=u"Емейл")

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)