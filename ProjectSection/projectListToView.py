from django.db import models
from django.conf import settings
from django.utils.html import strip_tags
from django.utils.html import escape
from django.templatetags.static import static
from .models import Projects

def generateProjectPageHtml():
    projectSet = Projects.objects.all()
    htmlStringLeft = ''
    htmlStringRight = ''

    projectCounter = 0
    for p in projectSet:
        # Two projects per row, start a row on even projects, end the row on odd
        if((projectCounter % 2) == 0):
            # Put the panel inside a row
            htmlStringLeft = htmlStringLeft + '<div class="row">'\
                            + generateProjectPanel(p.name, p.languages, p.descriptionFileLink, p.urlLink, (projectCounter / 6))\
                            + '</div>'
        else:
            # Put the panel inside a row
            htmlStringRight = htmlStringRight + '<div class="row">'\
                            + generateProjectPanel(p.name, p.languages, p.descriptionFileLink, p.urlLink, (projectCounter / 6))\
                            + '</div>'
        projectCounter = projectCounter + 1

    return { 'projectLeftHtml': htmlStringLeft, 'projectRightHtml': htmlStringRight, 'pageCount': ((projectCounter / 6) + 1) }

def generateProjectPanel(projectName, projectLanguages, descriptionFileLink, projectLink, pageNumber):
    # Sanitize incoming database entries
    projectName = strip_tags(projectName)
    projectLanguages = strip_tags(projectLanguages)
    descriptionFileLink = strip_tags(descriptionFileLink)
    projectLink = strip_tags(projectLink)

    projectName = escape(projectName)
    projectLanguages = escape(projectLanguages)
    descriptionFileLink = escape(descriptionFileLink)
    projectLink = escape(projectLink)

    projectDescription = ""

    # Open the file description, somewhere in the static file directory (unless the link is "N/A")
    # print(static(descriptionFileLink))
    if(descriptionFileLink == "N/A"):
        projectDescription = "No description available. Follow the link for more details."
    else:
        try:
            descFile = open(settings.STATIC_ROOT + descriptionFileLink, "r")
            projectDescription = descFile.read()
            descFile.close()
        except IOError:
            projectDescription = "Unable to load description. Please check back later."

    # Create the panel
    panelHtmlString = '<div class="panel panel-default pageControl_page-'+ str(pageNumber) +'">'\
\
                        + '<div class="panel-heading">'\
                            + '<h4>' + projectName + '</h4>'\
                            + '<h5>Languages: ' + projectLanguages + '</h5>'\
                        + '</div>'\
\
                        + '<div class="panel-body">'\
                            + '<p>' + projectDescription + '</p>'\
                            + '<a href="' + projectLink + '">' + projectLink + '</a>'\
                        + '</div>'\
\
                    + '</div>'

    return panelHtmlString
