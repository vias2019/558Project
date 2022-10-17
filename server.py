import socket
import threading
import time
import flask
 
class Server():
    def __init__(self):
        self.g_conn_pool = {}  # connection pool
        # record the number of client
        self.num = 0
        # server local address, would change to Azure IP address and port
        self.address = ('0.0.0.0', 8000)
        # initialize the server
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(self.address)
        self.server_socket.listen(128)
    def accept_client(self):
        """
            Receive new connection
            """
        while True:
            client_socket, info = self.server_socket.accept()  # blocking, waiting for client to connect
            print(client_socket,port)
            # create a single thread for each client
            thread = threading.Thread(target=self.recv_msg, args=(client_socket,info))
            thread.setDaemon(True)
            thread.start()
    def recv_msg(self,client,info):
        # prompt the server to start successfully
        print('Server is ready!！')
        client.sendall("connect server successfully!".encode(encoding='utf8'))
        # continuously accepting client connections
        while True:
            try:
                client.sendall(b'Success')
                while True:
                    msg = client.recv(1024)
                    msg_recv = msg.decode('utf-8')
                    if not msg_recv:
                        continue
                    else:
                        recv_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        print('Client ' + recv_time + ':\n')
                        print(' ' + msg_recv + '\n')
            except Exception as e:
 
                print('Client disconnects...')
                exit(-1)
                break
    def start_new_thread(self):
        """Start a new thread to receive information"""
        thread = threading.Thread(target=self.accept_client, args=())
        thread.setDaemon(True)
        thread.start()

# instantiate a Flask node
app = flask.Flask(__name__)
 
@app.route('/')
def hello():
    return 'hello'
 
if __name__ == '__main__':
 # create a parser
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5030, type=int, help='port to listen on')
    args = parser.parse_args()
    # get a port number
    port = args.port
    # instantiate a serverclass and start
    py_server = Server()
    py_server.start_new_thread()
    # start Flask node
    app.run(host='127.0.0.1',port=port)
