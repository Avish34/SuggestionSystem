from cleantext.clean import clean
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

'''
set_value function set the values of parameter needed for dialogflow object
'''
def set_value():
    project_id=os.getenv('PROJECT_ID')
    session_id=uuid.uuid1()
    language_code="en-US"
    return project_id,session_id,language_code

    
'''
helper function is used by get_suggestion to handle the request. 
It retunrs suggestion for the text provieded in argument.

'''
def helper(text):
    project_id,session_id,language_code=set_value()
    dialog_flow=DialogFlow(project_id,session_id,language_code)
    cleaned_text=TextCleaning(text)
    texts=cleaned_text.preprocess_text()
    value=dialog_flow.get_suggestions(texts)
    SaveText(text,value)
    return HttpResponse(value)

'''
accuracy function accepts list text as argument and returns accuracy of the model 
based on list of text given.
'''

def accuracy(texts):
    project_id,session_id,language_code=set_value()
    dialog_flow=DialogFlow(project_id,session_id,language_code)
    count=0
    cleaned_text=TextCleaning("")
    total_text=len(texts)
    for text in texts:
        cleaned_text.text=text[0]
        cleaned_text.santizie_notes()
        new_text=cleaned_text.text
        if(text[1]==dialog_flow.get_intent(new_text)):
            count+=1
    model_accuracy=(count/len(texts))*100
    response_object={"accuracy":model_accuracy,"total":total_text,"matched":count,"mismatched":total_text-count}
    return json.dumps(response_object)
