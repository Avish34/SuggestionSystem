from urllib import request
from google.cloud import dialogflow
from django.http import HttpResponse, JsonResponse, response
import json
from bs4.builder import HTML, HTML_5
from bs4 import BeautifulSoup
import nltk
from nltk import text
from nltk.tokenize import sent_tokenize
#nltk.download('punkt') Download once, then comment it!
from cleantext import clean
class DialogFlow:
    def __init__(self, project_id, session_id,language_code):
        self.project_id=project_id
        self.session_id=session_id
        self.language_code=language_code

    def get_suggestions(self,text):
        return self.detect_intent_texts(text)

    def get_intent(self,text):
        session_client = dialogflow.SessionsClient()

        session = session_client.session_path(self.project_id, self.session_id)
        text_input = dialogflow.TextInput(text=text, language_code=self.language_code)

        query_input = dialogflow.QueryInput(text=text_input)

        response = session_client.detect_intent(
                request={"session": session, "query_input": query_input}
            )

        print(response.query_result.intent.display_name)
        return response.query_result.intent.display_name
    
    def detect_intent_texts(self,text):
    
        session_client = dialogflow.SessionsClient()

        session = session_client.session_path(self.project_id, self.session_id)
        print("Session path: {}\n".format(session))
        suggestions=[]
        for texts in text:
            if(len(texts)>256):
                continue
            text_input = dialogflow.TextInput(text=texts, language_code=self.language_code)

            query_input = dialogflow.QueryInput(text=text_input)

            response = session_client.detect_intent(
                request={"session": session, "query_input": query_input}
            )

            print("=" * 20)
            print("Query text: {}".format(response.query_result.query_text))
            print(
                "Detected intent: {} (confidence: {})\n".format(
                response.query_result.intent.display_name,
                response.query_result.intent_detection_confidence,
                )
                )
            suggestions.append(response.query_result.fulfillment_text)
        send={"suggestion":suggestions}
        return json.dumps(send)    

class TextCleaning():
    def __init__(self,text):
        self.text=text

    def remove_extra_spaces(self):
        self.text=" ".join(self.text.split()) 

    def to_sentence(self):
        texts=sent_tokenize(self.text)
        return texts

    def clean_text(self):
        self.text=clean(self.text,no_phone_numbers=True)  
        print(self.text)  

    def preprocess_text(self):
        self.remove_extra_spaces()
        self.text=self.santizie_notes()
        return self.to_sentence()  

    def santizie_notes(self):
        soup = BeautifulSoup(self.text,features="html.parser")
        text = soup.get_text()
        print(text)
        return text    

          
