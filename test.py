import requests
import json

url = "http://127.0.0.1:5000/"
data = {'input': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data=json.dumps(data), headers=headers)

print(r.text)
# payload = {'number': 2, 'value': 1}
# r = requests.post("http://127.0.0.1:5000/", data={'input'='test'})