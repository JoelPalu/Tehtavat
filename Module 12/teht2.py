import requests

api_key = "06552479532843752b93e9c6dfccfa99"
city = input("Give city name: ")
# &units=metric muuttaa kelvinit celcius muotoon
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
re = requests.get(url).json()
print(f"City: {re['name']} \nTemperature: {re['main']['temp']} C \nWeather: {re['weather'][0]['description']}")

