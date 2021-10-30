import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"likes": 20, "name": "John", "views": 100000},
    {"likes": 0, "name": "Bill", "views": 100000},
    {"likes": 100000, "name": "Tom", "views": 100000}
]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE+"video/1")
print(response)
input()
response = requests.get(BASE + "video/6")
print(response.json())