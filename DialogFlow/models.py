from django.db import models

'''
Model for saving text and their corresponding actions
'''

class Suggestion(models.Model):
    Text=models.CharField(max_length=1000)
    Suggestions=models.JSONField()

