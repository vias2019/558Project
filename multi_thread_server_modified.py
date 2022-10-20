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
    
    def add(self, wordEng, wordSpa):
        object = dictionary.Translator()
        object.addDictionary(wordEng, wordSpa)
        return('Successfully added')
    
    def run(self): 
        while True : 
            data = conn.recv(1024) 
            if not data:
                print('Bye')
                break
            print(f"Server received data: {data}")
            
            opt = data.decode('utf-8')
            if opt == '01':
                data = conn.recv(1024)
                print(f"Server received data: {data}")
                word = data.decode('utf-8')
                rep = self.translate(word)
                reply = rep.encode('utf-8')
                conn.send(reply)
            else:
                with self.lock:
                    data = conn.recv(1024)
                    print(f"Server received data: {data}")
                    wordEng = data.decode('utf-8')
                    data = conn.recv(1024)
                    print(f"Server received data: {data}")
                    wordSpa = data.decode('utf-8')
                    rep = self.add(wordEng, wordSpa)
                    reply = rep.encode('utf-8')
                    conn.send(reply)

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
        
