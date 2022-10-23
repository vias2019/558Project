#client A
import socket 
from datetime import datetime

host = '127.0.0.1' 
port = 65432
BUFFER_SIZE = 1024
 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(b"hello")
    data = s.recv(BUFFER_SIZE)
    print('Received from the server :',str(data.decode('utf-8')), '--', datetime.now().strftime("%d-%m-%Y, %H:%M:%S"))