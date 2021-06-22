from django import http
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, response
from django.views.decorators.csrf import csrf_exempt
import json,uuid,os
from google.cloud import dialogflow
from google.cloud.dialogflow_v2.types import session
from .utility import DialogFlow
from .utility import TextCleaning
from .models import Suggestion
from .manager import SaveText

def set_value():
    project_id=os.getenv('PROJECT_ID')
    session_id=uuid.uuid1()
    language_code="en-US"
    return project_id,session_id,language_code


def helper(text):
    project_id,session_id,language_code=set_value()
    dialog_flow=DialogFlow(project_id,session_id,language_code)
    cleaned_text=TextCleaning(text)
    texts=cleaned_text.preprocess_text()
    value=dialog_flow.get_suggestions(texts)
    SaveText(text,value)
    return HttpResponse(value)

def accuracy(texts):
    project_id,session_id,language_code=set_value()
    dialog_flow=DialogFlow(project_id,session_id,language_code)
    count=0
    for text in texts:
        if(text[1]==dialog_flow.get_intent(text[0])):
            count+=1
    return (count/len(texts))*100
