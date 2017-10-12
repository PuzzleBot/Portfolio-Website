# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.
def embeddedProjectPage(request):
    return HttpResponse("Page Loaded")
