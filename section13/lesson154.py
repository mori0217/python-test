import requests

payload = {'key1': 'value1', 'key2': 'value2'}

base_url = 'http://httpbin.org/'

r = requests.get(base_url + 'get', params=payload)
print(r.status_code)
print(r.text)
print(r.json())

r = requests.post(base_url + 'post', data=payload)
print(r.status_code)
print(r.text)
print(r.json())

r = requests.put(base_url + 'put', data=payload)
print(r.status_code)
print(r.text)
print(r.json())

r = requests.delete(base_url + 'delete', data=payload)
print(r.status_code)
print(r.text)
print(r.json())
