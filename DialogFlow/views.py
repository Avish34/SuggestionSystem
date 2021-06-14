from django import http
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, response
from django.views.decorators.csrf import csrf_exempt
import json,uuid,os
from .utility import DialogFlow
from .utility import TextCleaning

def helper(text):

    project_id=os.getenv('PROJECT_ID')
    session_id=uuid.uuid1()
    language_code="en-US"
    dialog_flow=DialogFlow(project_id,session_id,language_code)
    cleaned_text=TextCleaning(text)
    texts=cleaned_text.preprocess_text()
    return dialog_flow.get_suggestions(texts)




def get_suggestion(request):
    
    if(request.method=='GET'):
        request_body = request.body.decode('utf-8')
        obj=json.loads(request_body)
        text=obj['note']
        if(len(text)==0):
            return HttpResponse(status=400)
        return helper(text)  
         
    return HttpResponse(status=405)

    
