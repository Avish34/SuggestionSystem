from django import http
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, response
from django.views.decorators.csrf import csrf_exempt
import json,uuid,os
from .utility import DialogFlow
from .utility import TextCleaning
from .models import Suggestion
from .handler import helper,accuracy,parse_file

'''
get_suggestion is the controller for /get_suggestion API endpoint used for getting response for
given text.
'''
def get_suggestion(request):
    
    if(request.method=='GET'):
        request_body = request.body.decode('utf-8')
        obj=json.loads(request_body)
        return helper(obj)  
         
    return HttpResponse(status=405)

'''
get_accuracy function handles the request for accuracy of the complete dataset.
'''
def get_accuracy(request):
    if(request.method=='GET'):
        return HttpResponse(accuracy())
         
    return HttpResponse(status=405)

'''
update_collection is the controller for /update_collection API endpoint which updates the database
which is used for computing accuracy of the model. 
'''

@csrf_exempt
def update_collection(request):
    upload = request.FILES['file']
    parse_file(upload)
    return HttpResponse(status=201)


'''
get_accuracy_patient is the controller for get_accuracy/patient?id= API endpoint. 
'''
def get_accuracy_patient(request):
    if(request.method=='GET'):
        return HttpResponse(accuracy(request.GET.get('id')))
         
    return HttpResponse(status=405)


