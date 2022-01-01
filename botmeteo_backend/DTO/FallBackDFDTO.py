from DTO.GlobalIntentDFDTO import GlobalIntentDFDTO


class FallBackDFDTO(GlobalIntentDFDTO):
    intent: None
    message: None

    def __init__(self, intent, message):
        super().__init__(intent,message)
