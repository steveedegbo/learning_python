
import requests

import json

api_key = "e421956a3aacb487aded7bab9194b623"

lat = "6.5244"

lon = "3.3792"

url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)

response = requests.get(url)

data = json.loads(response.text)

data = {'data' : data}

f = open("weather.py", "w")

f.write(json.dumps(data))

