from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
    template = loader.get_template('website/index.html')

    return HttpResponse(template.render("Hello, world. You're at the polls index."))
