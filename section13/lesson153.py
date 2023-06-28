import urllib.request
import urllib.parse
import json

payload = {'key1': 'value1', 'key2': 'value2'}

get_url = 'http://httpbin.org/get' + '?' + urllib.parse.urlencode(payload)
with urllib.request.urlopen(get_url) as f:
    print(json.loads(f.read().decode('utf-8')))

post_url = 'http://httpbin.org/post'
request_data = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(post_url, data=request_data, method='POST')
with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))

put_url = 'http://httpbin.org/put'
request_data = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(put_url, data=request_data, method='PUT')
with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))

delete_url = 'http://httpbin.org/delete'
request_data = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(delete_url, data=request_data, method='DELETE')
with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))
