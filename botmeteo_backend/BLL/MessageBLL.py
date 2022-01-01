from utils.ApiWeather import ApiWeather
from utils.ApiDialogFlow import ApiDialogFlow
import re
from datetime import datetime

#Variables globales
MESSAGES = {
    'message1': {'message': 'weather in Paris?', 'user':'userOne'},
    'message2': {'message': 'weather in Athens?', 'user':'userTwo'},
}
project_id = "Your project ID of Dialogflow"
session_id = "Your session ID"
language_code = "en-US"

#Gestion des erreurs
def abort_if_message_doesnt_exist(message_id):
    if message_id not in MESSAGES:
        return True
    else:
        False

def convert_date(date):
    get_date_string = re.search(r'\d{4}-\d{2}-\d{2}', date)
    extracted_date = datetime.strptime(get_date_string.group(), '%Y-%m-%d').date()
    return extracted_date

# def convert_time(date):
#     get_time_string = re.search(r'\d{2}:\d{2}:\d{2}', date)
#     extracted_time = datetime.strptime(get_time_string.group(), '%H:%M:%S').time()
#     return extracted_time.hour

class MessagedBLL():
    def getAll(self):
        return MESSAGES

    def getById(self, message_id):
        return MESSAGES[message_id]
    def post(self, args): 
        # 0. Stocker la réponse du user
        message_id = int(max(MESSAGES.keys()).lstrip('message')) + 1
        message_id = 'message%i' % message_id
        MESSAGES[message_id] = {'message': args['message'], 'user':args['user']}
        
        # 1. Récupérer le message dans args
        # 2. Envoyer le message à Dialog flow
        texts = args['message']
        dialogflow = ApiDialogFlow()
        response_dialog_flow = dialogflow.detect_intent_texts(project_id, session_id, texts, language_code)

        intent = response_dialog_flow.get_intent()
        message_df = response_dialog_flow.get_message()

        message = message_df  

        if(intent == "Weather Intent" and response_dialog_flow.get_all_required_fields()):
            city = response_dialog_flow.get_city()
            date = response_dialog_flow.get_date()
            # 3. Appeler l'API météo (externe)            
            # 4. construire une réponse en fonction de la météo
            if(date != ""):
                date_extrated = convert_date(date)        
                weather = ApiWeather.get_forecast(city, date_extrated)
                max_temperature_c = weather.get_max_temperature_c()
                min_temperature_c = weather.get_min_temperature_c()
                max_temperature_f = weather.get_max_temperature_f()
                min_temperature_f = weather.get_min_temperature_f()
                condition = weather.get_condition()
                # humidity = weather.get_humidity()
                #message
                message = message_df.capitalize() + ' in '+ city + ', the max temperature is ' + str(max_temperature_c)+'°C ('+str(max_temperature_f) + '°F) and the min temperature is ' + str(min_temperature_c)+'°C ('+str(min_temperature_f) + '°F). The weather is ' + condition.lower() +'.'
                response_dialog_flow.set_message(message)
            else:
                weather = ApiWeather.get_current(city)
                temperature_c = weather.get_temperature_c()
                temperature_f = weather.get_temperature_f()
                condition =  weather.get_condition()
                # humidity = weather.get_humidity()
                #message
                message = 'In '+ city + ', the temperature is '+ str(temperature_c)+'°C ('+str(temperature_f) + '°F) and the weather is '+ condition.lower() +'.'
                response_dialog_flow.set_message(message)

        # 5. On stocke le message du bot dans la liste
        message_id = int(max(MESSAGES.keys()).lstrip('message')) + 1
        message_id = 'message%i' % message_id
        message_bot = {'message': message, 'user':'BOT'}
        MESSAGES[message_id] = message_bot

        return message_bot
        
    def put(self, message_id, args):
        MESSAGES[message_id] = {'message':args['message'], 'user':args['user']}
        return MESSAGES[message_id]

    def delete(self, message_id):
        del MESSAGES[message_id]
        return ''