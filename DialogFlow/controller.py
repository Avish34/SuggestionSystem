from django import http
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, response
from django.views.decorators.csrf import csrf_exempt
import json,uuid,os
from .utility import DialogFlow
from .utility import TextCleaning
from .models import Suggestion
from .handler import helper,accuracy,parse_file


def get_suggestion(request):
    
    if(request.method=='GET'):
        request_body = request.body.decode('utf-8')
        obj=json.loads(request_body)
        text=obj['note']
        if(len(text)==0):
            return HttpResponse(status=400)
        return helper(text)  
         
    return HttpResponse(status=405)

'''
get_accuracy function handles the request for accuracy.
'''
def get_accuracy(request):
    if(request.method=='GET'):
        return HttpResponse(accuracy())
         
    return HttpResponse(status=405)

@csrf_exempt
def update_collection(request):
    upload = request.FILES['file']
    parse_file(upload)
    return HttpResponse('ok')

def get_accuracy_patient(request):
    if(request.method=='GET'):
        return HttpResponse(accuracy(request.GET.get('id')))
         
    return HttpResponse(status=405)


