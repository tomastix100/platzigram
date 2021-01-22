"""Platzigram views."""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json


def hello_world(request):
    """Return a greeting."""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    respuesta = 'Oh, hi! Current server time is {now}'.format(
        now=now
        )
    return HttpResponse(respuesta)
    # Es lo mismo pero mas resumido
    """ 
    return HttpResponse('Oh, hi! Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))
    """


def hi(request):
    """Hi."""
    lista_ordenada = sorted([int(x) for x in request.GET['numbers'].split(',')])
    data = {
        'status':'ok',
        'numbers':lista_ordenada,
        'message':'Integers sorted successfully.'
    }
    
    return HttpResponse(json.dumps(data), content_type='application/json')
