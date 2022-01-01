from DTO.GlobalIntentDFDTO import GlobalIntentDFDTO


class WelcomeDFDTO(GlobalIntentDFDTO):

    def __init__(self, intent, message):
        super().__init__(intent, message)
