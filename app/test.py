import requests

BASE = "http://localhost:5000/"

response = requests.get(BASE+ "api/v1/facilities/10/relation/2613782")
print(response.json())