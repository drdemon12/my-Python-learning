import requests
import json

b = requests.get("https://jsonplaceholder.typicode.com/todos")
b = json.loads(b.text) # loads liste yapar text ise mesajı alır

for i in b:
    print(i)