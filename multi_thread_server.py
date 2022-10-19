import socket 
from threading import Thread 
from threading import Lock
import dictionary

# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread): 
    lock = Lock()
    def __init__(self,ip,port,conn): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port
        self.conn = conn
        print(f"[+] New server socket thread started for ip:{ip} and port: {port}")
    
    def translate (self, str):
        object = dictionary.Translator()
        return(object.searchDictionary(str))
    
    def run(self): 
        while True : 
            data = conn.recv(2048) 
            print(f"Server received data: {data}")
            if not data:
                break
            with self.lock:
#You can uncomment the following two line to elongate the process and see the effect of multithreading
                # for _ in range(50000000):
                #     a = 2 ** 100
                    t = (data.decode('ascii')).lower()
                    print(t)
                    temp=self.translate(t)
                    data=temp.encode('ascii')
                    self.conn.send(data) 
    
    # def translate (str):
    #     object = dictionary.Translator()
    #     return(object.searchDictionary(str))
           

# Multithreaded Python server : TCP Server Socket Program Stub
TCP_IP = 'localhost' 
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
        
