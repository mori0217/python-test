import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind("tcp://127.0.0.1:5690")

id = 0
while True:
    id += 1
    socket.send_string(str(id))
    print("Sent: ", id)
    time.sleep(1)
