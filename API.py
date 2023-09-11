import requests
import json

apiKey = "f368dd14592386a0e3051328b54a9fce"

baseUrl = "https://v3.football.api-sports.io/"

headers = {
    "x-apisports-key" : apiKey
}

endpoint = "countries"

url = baseUrl + endpoint

params = {
    "code" : "IT"
}
response = requests.get(url=url, headers=headers, params=params)
# print(response.status_code)
# print(response.text)

dictionary = response.json()["response"]
print(dictionary)

for e in dictionary:
    print(e["name"], e["code"])
# print(json.dumps(dictionary, indent=4))


# print("Make a request to this url: {}".format(url))