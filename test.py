import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 72, "name": "Joe jokes", "views": 4200}, 
{"likes": 21, "name": "crazzyKoding Montage", "views": 66600},
 {"likes":  700000, "name": "how to reverse a linked list ", "views": 9292922} ]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())


input()
response = requests.get(BASE + "video/2")
print(response.json())