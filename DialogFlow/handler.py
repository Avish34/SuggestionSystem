from bs4.builder import HTML, HTML_5
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
from bs4 import BeautifulSoup

def set_value():
    project_id=os.getenv('PROJECT_ID')
    session_id=uuid.uuid1()
    language_code="en-US"
    return project_id,session_id,language_code

def santizie_notes(text):
    soup = BeautifulSoup(text,features="html.parser")
    text = soup.get_text()
    print(text)
    return text
    

def helper(text):
    project_id,session_id,language_code=set_value()
    text=santizie_notes(text)
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
        text=santizie_notes(text[0])
        if(text[1]==dialog_flow.get_intent(text)):
            count+=1
    return (count/len(texts))*100
