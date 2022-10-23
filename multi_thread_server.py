import socket 
from threading import Thread 
from threading import Lock
import dictionary
import threading, time, random
from datetime import datetime

mutex = threading.Lock()
# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread): 
    def __init__(self,ip,port,conn): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port
        self.conn = conn
        print(f"[+] New server socket thread started for ip:{ip} and port: {port}", '--', datetime.now().strftime("%d-%m-%Y, %H:%M:%S"))

    def translate (self, str):
        object = dictionary.Translator()
        return(object.searchDictionary(str))
    
    def run(self): 
        while True : 
            data = conn.recv(2048) 
            print(f"Server received data: {data}", '--', datetime.now().strftime("%d-%m-%Y, %H:%M:%S"))
            if not data:
                break
            mutex.acquire()
            # You can uncomment the following two line to elongate the process and see the effect of multithreading
            time.sleep(random.randint(1, 5))
            t = (data.decode('utf-8')).lower()
            temp = self.translate(t)
            data = temp.encode('utf-8')
            mutex.release()
            self.conn.send(data) 
           

# Multithreaded Python server : TCP Server Socket Program Stub
TCP_IP = '127.0.0.1'
TCP_PORT = 65432
BUFFER_SIZE = 1024  # Usually 1024, but we need quick response 


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    s.bind((TCP_IP, TCP_PORT)) 

    while True: 
        s.listen() 
        print("Multithreaded Python server : Waiting for connections from TCP clients...")
        (conn, (ip,port)) = s.accept() 
        newthread = ClientThread(ip,port,conn) 
        newthread.start() 
        