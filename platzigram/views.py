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


def sort_integers(request):
    """Retuturns a JSON reponse with sorted intergers"""
    lista_ordenada = sorted([int(x) for x in request.GET['numbers'].split(',')])
    data = {
        'status':'ok',
        'numbers':lista_ordenada,
        'message':'Integers sorted successfully.'
    }
    # El metodo json.dumps({}) traduce un diccionario de python a Json, si
    # queremos que tenga una indentacion lo que hace,os es agregar el paraemtro
    # *indent*
    return HttpResponse(
        json.dumps(
            data, 
            indent=4
        ), 
        content_type='application/json'
    )

def say_hi(request, name, age):
    """Retirn a greeting"""
    if age < 12:
        message = 'Sorry {}, you are not allowed here.'.format(name)
    else:
        message = 'Helo, {}! Welcome to Platzigram.'.format(name)
    return HttpResponse(message)
