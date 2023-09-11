import requests
import json

apiKey = "f368dd14592386a0e3051328b54a9fce"

baseUrl = "https://v3.football.api-sports.io/"

headers = {"x-apisports-key": apiKey}

endpoint = {"timezone": "timezone", "leagues": "leagues", "countries": "countries"}

url = baseUrl + endpoint["countries"]

print(url)

params = {"code"}
response = requests.get(url=url, headers=headers)
# print(response.status_code)
# print(response.text)

dictionary = response.json()["response"]
print(dictionary)


for el in dictionary:
    url = el["flag"]
    print(url)


# code to save img to file(using PIL lib)
