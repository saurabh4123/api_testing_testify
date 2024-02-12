from urllib.request import urlopen

# #to receive html response
# with urlopen("https://www.example.com") as response:
#     body=response.read()

# print(body)  #body is html response

import json
url="https://jsonplaceholder.typicode.com/todos/1"
with urlopen(url) as response:
    body=response.read()

todo_item=json.loads(body)  #translates returned json bytes into python dictionary
print(todo_item)
