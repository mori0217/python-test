import zmq

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.connect("tcp://127.0.0.1:5690")

while True:
    message = socket.recv()
    print("Received: ", message)
