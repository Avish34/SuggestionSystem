from django import http
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, response
from django.views.decorators.csrf import csrf_exempt
import json,uuid,os
from .utility import DialogFlow
from .utility import TextCleaning
from .models import Suggestion
from .manager import SaveText

def helper(text):

    project_id=os.getenv('PROJECT_ID')
    session_id=uuid.uuid1()
    language_code="en-US"
    dialog_flow=DialogFlow(project_id,session_id,language_code)
    cleaned_text=TextCleaning(text)
    texts=cleaned_text.preprocess_text()
    value=dialog_flow.get_suggestions(texts)
    SaveText(text,value)
    return HttpResponse(value)