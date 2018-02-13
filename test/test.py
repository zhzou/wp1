import json
import urllib.request

data = { 'grid': ['O','O',' ','X',' ',' ',' ','X','X'],'winner':' '}

req = urllib.request.Request('http://127.0.0.1:8000/play/')
req.add_header('Content-Type','application/json')

response = urllib.request.urlopen(req, json.dumps(data).encode('utf8'))
print(response.read().decode('utf-8'))