from .models import Suggestion

def SaveText(text,response):
    obj=Suggestion(Text=text,Suggestions=response)
    obj.save()
    return
