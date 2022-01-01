from DTO.GlobalIntentDFDTO import GlobalIntentDFDTO


class ThanksIntentDFDTO(GlobalIntentDFDTO):

    def __init__(self, intent, message):
        super().__init__(intent, message)