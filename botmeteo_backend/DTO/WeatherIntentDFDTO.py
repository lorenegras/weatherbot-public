from DTO.GlobalIntentDFDTO import GlobalIntentDFDTO

class WeatherIntentDFDTO(GlobalIntentDFDTO):
    city: None
    date: None

    def __init__(self, query_result):
        super().__init__(query_result)
        self.city = query_result.parameters["geo-city"]
        self.date = query_result.parameters["date-time"]

    def get_city(self):
        return self.city

    def get_date(self):
        return self.date
    
    def set_city(self, city):
        self.city = city

    def set_date(self, date):
        self.date = date