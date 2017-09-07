from django.http import HttpResponse
from django.template import loader
from . import settings


def index(request):
    frontBodyLink = "textFiles/frontBodyText.txt"
    template = loader.get_template('index.html')

    try:
        descFile = open(settings.STATIC_ROOT + frontBodyLink, "r")
        bodyText = descFile.read()
        descFile.close()
    except IOError:
        bodyText = "Whoops! We couldn't load the text for this part. Please check back later."

    context = { 'frontPageBody' : bodyText }
    return HttpResponse(template.render(context, request))
