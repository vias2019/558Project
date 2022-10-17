#client A
import socket 

host = '127.0.0.1' 
port = 65432
BUFFER_SIZE = 1024
 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(b"Happy Monday!")
    data = s.recv(BUFFER_SIZE)
    print(f"Received {data!r}")