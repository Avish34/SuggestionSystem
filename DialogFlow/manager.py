from .models import Suggestion
from .models import accuracy_db
'''
SaveText function helps to save the data in database by accepting text and 
response(suggestion) as parameter.
'''
def SaveText(Patient_id,Note_id,text,response):
    obj=Suggestion(Patient_id=Patient_id,Note_id=Note_id,Text=text,Suggestions=response)
    obj.save()
    return

'''
save_in_accuracy helps to save data in database by taking patient_id, text
and intent as parameter.
'''
def save_in_accuracy(patient_id, text, intent):
    obj=accuracy_db(Patient_id=patient_id,Text=text,Intent=intent)
    obj.save()
    return    
