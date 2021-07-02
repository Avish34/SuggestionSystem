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
from .manager import SaveText,save_in_accuracy
import pandas as pd
import csv
from .models import accuracy_db 


def get_queryset(patient_id=-1):
    if(patient_id==-1):
         return accuracy_db.objects.filter()
    return accuracy_db.objects.filter(Patient_id=patient_id)     


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
def helper(obj):
    project_id,session_id,language_code=set_value()
    text=obj['note']
    Patient_id=obj['patient_id']
    Note_id=obj['note_id']
    dialog_flow=DialogFlow(project_id,session_id,language_code)
    cleaned_text=TextCleaning(text)
    texts=cleaned_text.preprocess_text()
    value=dialog_flow.get_suggestions(texts)
    SaveText(Patient_id,Note_id,text,value)
    return HttpResponse(value)

'''
accuracy function accepts list text as argument and returns accuracy of the model 
based on list of text given.
'''

def accuracy(patient_id=-1):
    project_id,session_id,language_code=set_value()
    dialog_flow=DialogFlow(project_id,session_id,language_code)
    count=0
    len=0
    obj=get_queryset(patient_id)
    for text in obj.iterator():
        if(text.Intent==dialog_flow.get_intent(text.Text)):
            count+=1
        len+=1    
        
    model_accuracy=(count/len)*100
    response_object={"accuracy":model_accuracy,"total":len,"matched":count,"mismatched":len-count}
    return json.dumps(response_object)



def parse_file(file):
    decoded_file = file.read().decode('utf-8-sig').splitlines()
    reader = csv.DictReader(decoded_file)
    cleaned_text=TextCleaning("")
    for row in reader:
        cleaned_text.text=row['Text']
        cleaned_text.santizie_notes()
        save_in_accuracy(row['Patient_id'],cleaned_text.text,row['Intent'])

    
       