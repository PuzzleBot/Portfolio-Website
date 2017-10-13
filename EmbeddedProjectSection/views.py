# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.
def embeddedProjectPage(request):
    template = loader.get_template("embeddedProjectIndex.html")

    context = {}

    return HttpResponse(template.render(context, request))
