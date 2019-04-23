# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here
class CoursePageViews(models.Model):
    reg_no = models.CharField(max_length=9)
    timestamps = models.TextField()

class MarkPageViews(models.Model):
    reg_no = models.CharField(max_length=9)
    timestamps = models.TextField()

class MainPageViews(models.Model):
    reg_no = models.CharField(max_length=9)
    timestamps = models.TextField()
    
