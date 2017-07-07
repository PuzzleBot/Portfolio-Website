# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Projects(models.Model):
    name = models.CharField(max_length=200)
    languages = models.CharField(max_length=200)
    dateStart = models.DateField()
    dateEnd = models.DateField()
    urlLink = models.CharField(max_length=500)
    descriptionFileLink = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    ordering = ['-dateStart']

    def __str__(self):
        return self.name + ", " + self.urlLink

    class Meta:
        verbose_name_plural = 'Projects'
