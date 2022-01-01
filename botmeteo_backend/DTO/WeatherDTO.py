class WeatherDTO():
    temperature_c: None
    max_temperature_c: None
    min_temperature_c: None
    temperature_f: None
    max_temperature_f: None
    min_temperature_f: None
    condition: None
    humidity: None

    def __init__(self, temperature_c, max_temperature_c, min_temperature_c, temperature_f, max_temperature_f, min_temperature_f, condition, humidity):
        self.temperature_c = temperature_c
        self.max_temperature_c = max_temperature_c
        self.min_temperature_c = min_temperature_c
        self.temperature_f = temperature_f
        self.max_temperature_f = max_temperature_f
        self.min_temperature_f = min_temperature_f
        self.condition = condition
        self.humidity = humidity

    def get_temperature_c(self):
        return self.temperature_c

    def get_max_temperature_c(self):
        return self.max_temperature_c

    def get_min_temperature_c(self):
        return self.min_temperature_c


    def get_temperature_f(self):
        return self.temperature_f

    def get_max_temperature_f(self):
        return self.max_temperature_f

    def get_min_temperature_f(self):
        return self.min_temperature_f

    def get_condition(self):
        return self.condition

    def get_humidity(self):
        return self.humidity