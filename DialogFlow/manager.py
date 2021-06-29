from .models import Suggestion
'''
SaveText function helps to save the data in database by accepting text and response(suggestion) as argument
'''
def SaveText(text,response):
    obj=Suggestion(Text=text,Suggestions=response)
    obj.save()
    return
