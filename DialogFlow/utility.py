from google.cloud import dialogflow
from django.http import HttpResponse, JsonResponse, response
import json

class DialogFlow:
    def __init__(self, project_id, session_id,language_code):
        self.project_id=project_id
        self.session_id=session_id
        self.language_code=language_code

    def getSuggestion(self,text):
        return HttpResponse(self.detect_intent_texts(text))

    def detect_intent_texts(self,texts):
    
        session_client = dialogflow.SessionsClient()

        session = session_client.session_path(self.project_id, self.session_id)
        print("Session path: {}\n".format(session))

        
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
        
        send={"suggestion":response.query_result.fulfillment_text}
        return json.dumps(send,indent=4)    
