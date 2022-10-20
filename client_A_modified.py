#client A
import socket 

host = '' 
port = 65432
BUFFER_SIZE = 1024
 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    while True:
        opt = input('\nchoose you option, 01 for translation, 02 for adding:')
        s.send(opt.encode('ascii'))   # message send to server
        if opt == "01":
            word = input('\nPlease enter the word to translate:')
            s.send(word.encode('ascii'))
            data = s.recv(1024)  # receive from server
            print('Received from the server :',str(data.decode('ascii')))
        else:
            wordEng = input('\nPlease enter the word in English:')
            s.send(wordEng.encode('ascii'))
            wordSpa = input('\nPlease enter the word in Spanish:')
            s.send(wordSpa.encode('ascii'))
            data = s.recv(1024)
            print('Received from the server :',str(data.decode('ascii')))
        
        # ask the client whether he wants to continue
        ans = input('\nDo you want to continue(y/n) :')
        if ans == 'y':
            continue
        else:
            break

