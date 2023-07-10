import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt_string(zmq.SUBSCRIBE, "sub:1:")
socket.connect("tcp://127.0.0.1:5690")

while True:
    message = socket.recv()
    print("Received: ", message)
