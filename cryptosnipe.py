import requests

def requestData(): 
    r = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    return r.json()

print(requestData())