from urllib import request
from google.cloud import dialogflow
from django.http import HttpResponse, JsonResponse, response
import json
from bs4.builder import HTML, HTML_5
from bs4 import BeautifulSoup
import nltk
from nltk import text
from nltk.tokenize import sent_tokenize
from cleantext import clean
#nltk.download('punkt') Download once, then comment it!


'''
DialogFlow class offers functionality like getting intents or suggestion for a text.
'''

class DialogFlow:
    # Intialization of class variables
    def __init__(self, project_id, session_id,language_code):
        self.project_id=project_id
        self.session_id=session_id
        self.language_code=language_code

    # returns suggestion for text by calling DialogFlow API throigh detect_intent_texts
    def get_suggestions(self,text):
        return self.detect_intent_texts(text)

    # returns the intent for corresponding text
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

    # DialogFlow API used to get suggestions
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

'''
A text processing class with functionality like santizing text,
 removing white spaces and diving text into sentences.
'''

class TextCleaning():
    # Intialization of class variables
    def __init__(self,text):
        self.text=text

    # Remove Extra space from sentences
    def remove_extra_spaces(self):
        self.text=" ".join(self.text.split()) 

    # Genrate all sentence from given text. 
    def to_sentence(self):
        texts=sent_tokenize(self.text)
        return texts

    # Used to remove phone numbers from text
    def clean_text(self):
        self.text=clean(self.text,no_phone_numbers=True)  
        print(self.text)  

    # Use of all above function in one function
    def preprocess_text(self):
        self.remove_extra_spaces()
        self.text=self.santizie_notes()
        return self.to_sentence()  

    # Clear HTML tags from sentences
    def santizie_notes(self):
        soup = BeautifulSoup(self.text,features="html.parser")
        text = soup.get_text()
        print(text)
        return text    

          
