import sys
import requests
import json

url = "https://api.meaningcloud.com/sentiment-2.1"

x = {'key': '8601f345cb8241110b493ab5e4fc7736', 
    'lang': 'auto',
    'txt': '@TayaPYT thanx babe .. Xoxo .. See u in a second',
    'ilang': 'en'}
headers = {'content-type': 'application/json'}

response = requests.request("POST", url, data=json.dumps(x), headers=headers)

y = json.loads(response.text)

print(y['confidence'])