import socket

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind(('127.0.0.1', 50007))
#     s.listen(1)
#     while True:
#         print("Waiting for connection...")
#         conn, addr = s.accept()
#         with conn:
#             print(f"Connected by {addr}")
#             while True:
#                 data = conn.recv(1024)
#                 if not data:
#                     break
#                 print(f"data:{data}, addr:{addr}")
#                 conn.sendall(b'Received: ' + data)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(('127.0.0.1', 50007))
    while True:
        print("Waiting for connection...")
        data, addr = s.recvfrom(1024)
        print(f"Connected by {addr}")
        print(f"data:{data}, addr:{addr}")
