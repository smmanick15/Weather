# Import the JSON library.
import json

# Import the requests library.
import requests

# Declaring parameters
params = {
  'access_key': 'c02866b1a0e5bbbe58fa8054d4ed5495',
  'query': 'Cupertino, California'
}


response = requests.get("http://api.weatherstack.com/current?units=f", params)

response_code = response.status_code

print(response_code)
print(type(response))

json_data = response.json()

print(type(json_data))

print(json_data)

for key in json_data['current']:
  print(key, " ----> ", json_data['current'][key])

print("\n\nNow printing all of the response keys:\n")

for key in json_data:
  print(key, " ----> ", json_data[key])

print("\n\nThe weather in your query feels like: ", json_data['current']['weather_descriptions'])

#print(json_data['current'])


