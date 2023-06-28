from xmlrpc.server import SimpleXMLRPCServer

with SimpleXMLRPCServer(('localhost', 8000)) as server:
    def add(x, y):
        return x + y
    server.register_function(add)
    server.serve_forever()
