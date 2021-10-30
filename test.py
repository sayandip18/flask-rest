import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "video/0", {"likes": 20, "name": "John", "views": 100000})
print(response.json())

input()
response = requests.delete(BASE+"video/0")
print(response)
input()
response = requests.get(BASE + "video/6")
print(response.json())