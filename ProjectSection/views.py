# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Projects
from .projectListToView import generateProjectPageHtml

# Create your views here.
def projectPage(request):
    template = loader.get_template('project.html')

    # Get project entries from the database, format them into html elements
    context = generateProjectPageHtml()

    return HttpResponse(template.render(context, request))
