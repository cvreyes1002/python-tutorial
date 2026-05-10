
# c61d71a00ad5657345ca7772ba0da987
# http://api.openweathermap.org/data/2.5/forecast?lat=44.34&lon=10.99&appid=c61d71a00ad5657345ca7772ba0da987
import requests

parameters = {
    "lat": 14.50,
    "lon": 121.03,
    "appid": "c61d71a00ad5657345ca7772ba0da987"

}

response = requests.get(url="http://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
