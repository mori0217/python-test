import xmlrpc.client

with xmlrpc.client.ServerProxy('http://localhost:8000') as proxy:
    print(proxy.add(200, 3))
