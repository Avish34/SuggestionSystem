from django.db import models

class Suggestion(models.Model):
    Text=models.CharField(max_length=1000)
    Suggestions=models.JSONField()

