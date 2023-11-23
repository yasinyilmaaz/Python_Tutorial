import requests
import json
#  sitelerden veri çekmemiz gerekirse kullanılan kütüphane

result = requests.get("https://jsonplaceholder.typicode.com/todos")
result = json.loads(result.text)

for i in result:
    if i["userId"] == 1: 
        print(i["title"])

print(type(result))

