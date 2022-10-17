import json
import socket
import threading
import time
import struct

class Client():
 
    def __init__(self):
     # server IP address and port
        self.server_address = ('127.0.0.1', 8000)
         
        self.num = 0
    def recv_msg(self):
        print("connecting to server....")
 
        # client connects to server
        while True:
            try:
                self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # connect to server
                self.client_socket.connect(self.server_address)
 
                num = self.num
 
                # create header
                header_dic = {
                    'filename': num
                }
                header_bytes = json.dumps(header_dic).encode('utf-8')
                self.client_socket.send(struct.pack('i', len(header_bytes)))
                self.client_socket.send(header_bytes)
                 
    # receive message
                while True:
                    msg_recv = self.client_socket.recv(1024).decode('gbk')
                    print(msg_recv)
 
                    if msg_recv == 'Success':
                        print('The client has successfully established a connection with the server...')
                    elif not msg_recv:
                        continue
                    else:
                        recv_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        print( 'Server ' + recv_time + ':\n')
                        print(' ' + msg_recv + '\n')
 
            except:
                print('Disconnect with server...')
                break
    def start_new_thread(self):
        """start a new thread to receive message"""
        thread = threading.Thread(target=self.recv_msg, args=())
        thread.setDaemon(True)
        thread.start()
         
def main():
    wf = Client()
    wf.start_new_thread()
    while True:
        a = input()
        wf.client_socket.send(a.encode('utf-8'))
 
if __name__ == '__main__':
 
    main()