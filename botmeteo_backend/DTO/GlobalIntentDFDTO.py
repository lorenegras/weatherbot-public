class GlobalIntentDFDTO():
    intent: None
    message: None
    all_required_fields: False

    def __init__(self, query_result):
        self.intent = query_result.intent.display_name
        self.message = query_result.fulfillment_messages[0].text.text[0]
        self.all_required_fields = query_result.all_required_params_present

    def get_intent(self):
        return self.intent

    def get_message(self):
        return self.message

    def get_all_required_fields(self):
        return self.all_required_fields

    def set_intent(self, intent):
        self.intent = intent
    
    def set_message(self, message):
        self.message = message