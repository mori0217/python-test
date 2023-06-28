import requests

r = requests.get("http://127.0.0.1:5000/post", params={"key1": "value1", "key2": "value2"})
print(r.text)

r = requests.post("http://127.0.0.1:5000/post", data={"key1": "value1", "key2": "value2"})
print(r.text)

r = requests.put("http://127.0.0.1:5000/post", data={"key1": "value1", "key2": "value2"})
print(r.text)

r = requests.delete("http://127.0.0.1:5000/post", data={"key1": "value1", "key2": "value2"})
print(r.text)
