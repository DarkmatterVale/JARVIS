from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib import messages

from jarvis import Jarvis

YOLO = "TEST"

def index(request):
    template = loader.get_template('website/index.html')

    #YOLO = "YOLO TEST"

    return HttpResponse(template.render({'YOLO' : YOLO}))

def get_response(request):
    messages.add_message(request, messages.INFO, 'Hello world.')
    template = loader.get_template('website/index.html')
    YOLO = request.POST['choice']
    print request.POST['choice']
    return HttpResponseRedirect(template.render({'YOLO' : request.POST['choice']}))
