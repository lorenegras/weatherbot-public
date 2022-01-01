from google.cloud import dialogflow
from DTO.GlobalIntentDFDTO import GlobalIntentDFDTO
from DTO.WeatherIntentDFDTO import WeatherIntentDFDTO

class ApiDialogFlow():
    def detect_intent_texts(self, project_id, session_id, texts, language_code):
        session_client = dialogflow.SessionsClient()

        session = session_client.session_path(project_id, session_id)
        print("Session path: {}\n".format(session))

        text_input = dialogflow.TextInput(text=texts, language_code=language_code)
        query_input = dialogflow.QueryInput(text=text_input)

        response = session_client.detect_intent(request={"session": session, "query_input": query_input})
        
        global_intent = GlobalIntentDFDTO(response.query_result)
        if(global_intent.get_intent() == "Weather Intent"):
            response_dialog_flow = WeatherIntentDFDTO(response.query_result)
        else:
            response_dialog_flow = global_intent
            
        return response_dialog_flow
