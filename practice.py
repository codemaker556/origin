import requests
import json

response = requests.get("https://a.4cdn.org/s/thread/20593800")
print(response.status_code)
#print(response.json())
fox = response.json()
print(fox["image"])