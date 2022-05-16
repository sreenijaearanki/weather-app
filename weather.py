import json
import urllib


def getWeatherData():
  
    #enter the api key here
    api = 'db95b5bf37f6d714678d69e1ba86d6c2'
    
    cityList = ['London','Hyderabad','Rome','Paris','Vienna','Delhi','Mumbai','Kolkata','Moscow','Dubai','Tokyo','Singapore','Nashville','Barcelona','Madrid','Amsterdam','Toronto','Sydney','Hamburg','Berlin','Washington','Istanbul','Beijing','Prague','Milan','Boston','Dublin','Budapest','Bangkok','Athens']
    #creating an empty dictionary to store the weather data
    weatherData = {}
    
    for city in cityList :
        # source contain json data from api
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api).read()

        # converting JSON data to a dictionary
        list_of_data = json.loads(source)

        # data for variable list_of_data
        data = {
        "country_code": str(list_of_data['sys']['country']),
            "city_name": str(list_of_data['name']),
            "coordinate": str(list_of_data['coord']['lon']) + '; ' 
                    + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "temp_cel": str(round(list_of_data['main']['temp'] - 273.15)) + '°C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
        #print the weather data to the console
        print(data)
        
        weatherData[city] = data
    return weatherData