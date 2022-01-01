import requests
from DTO.WeatherDTO import WeatherDTO

class ApiWeather():
    def get_current(city):
        url = "https://weatherapi-com.p.rapidapi.com/current.json"
        querystring = {"q":city}
        headers = {
            'x-rapidapi-host': "Your host",
            'x-rapidapi-key': "Your ID of weather API"
            }
        response = requests.request("GET", url, headers=headers, params=querystring).json()
        temperature_c = response.get('current').get('temp_c')
        temperature_f = response.get('current').get('temp_f')
        condition = response.get('current').get('condition').get('text')
        humidity = response.get('current').get('humidity')
        weathercurrent = WeatherDTO(temperature_c, None, None, temperature_f, None, None, condition, humidity)
        return weathercurrent
    
    def get_forecast(city, date):
        url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
        querystring = {"q":city, "dt":date}
        headers = {
            'x-rapidapi-host': "Your host",
            'x-rapidapi-key': "Your ID of weather API"
            }
        response = requests.request("GET", url, headers=headers, params=querystring).json()
        max_temperature_c = response.get('forecast').get('forecastday')[0].get('day').get('maxtemp_c')
        min_temperature_c = response.get('forecast').get('forecastday')[0].get('day').get('mintemp_c')
        max_temperature_f = response.get('forecast').get('forecastday')[0].get('day').get('maxtemp_f')
        min_temperature_f = response.get('forecast').get('forecastday')[0].get('day').get('mintemp_f')
        condition = response.get('forecast').get('forecastday')[0].get('day').get('condition').get('text')
        humidity = response.get('forecast').get('forecastday')[0].get('day').get('avghumidity')
        weatherforecast = WeatherDTO(None,max_temperature_c,min_temperature_c, None, max_temperature_f,min_temperature_f,condition, humidity)
        return weatherforecast
