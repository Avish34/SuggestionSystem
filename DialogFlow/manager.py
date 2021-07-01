from .models import Suggestion
from .models import accuracy_db
'''
SaveText function helps to save the data in database by accepting text and 
response(suggestion) as argument.
'''
def SaveText(text,response):
    obj=Suggestion(Text=text,Suggestions=response)
    obj.save()
    return

def save_in_accuracy(patient_id, text, intent):
    obj=accuracy_db(Patient_id=patient_id,Text=text,Intent=intent)
    obj.save()
    return    
