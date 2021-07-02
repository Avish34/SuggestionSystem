from django.db import models

'''
Model for saving patient_id,note_id ,text and their corresponding actions
'''

class Suggestion(models.Model):
    Patient_id=models.IntegerField()
    Note_id=models.IntegerField()
    Text=models.CharField(max_length=1000)
    Suggestions=models.JSONField()

'''
Model for saving data for computing accuracy
'''
class accuracy_db(models.Model):
    Patient_id=models.IntegerField()
    Text=models.CharField(max_length=1000)
    Intent=models.CharField(max_length=1000)



