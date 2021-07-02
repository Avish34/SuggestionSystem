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


'''
get_queryset function returns query set from mongodb based on the patient_id. if patient_id is -1
then we need to get all the data from database.
'''
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
accuracy function accepts patient_id as parameter and returns accuracy corresponding to
the patient_id. if patient_id is -1 then we need to compute accuract for complete data.
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

'''
parse_file function takes file as a csv file as argument , parse and cleans the text content . 
And saves the content of csv file into database.
'''

def parse_file(file):
    decoded_file = file.read().decode('utf-8-sig').splitlines()
    reader = csv.DictReader(decoded_file)
    cleaned_text=TextCleaning("")
    for row in reader:
        cleaned_text.text=row['Text']
        cleaned_text.santizie_notes()
        save_in_accuracy(row['Patient_id'],cleaned_text.text,row['Intent'])

    
       