import socket
import os
from _thread import *


count=0
player1ships=[]
player2ships=[]

def startserver():
    serv=socket.socket()
    host='127.0.0.1'
    port = 1233
    ThreadCount = 0
    try:
        serv.bind((host,port))
    except socket.error as e:
        print(str(e))

    print("waiting for connection..")
    serv.listen(5)

    def threadclient(connection,player):
        connection.send(str.encode("hello from server"))
        while True:
            data = connection.recv(2048)
            reply = 'server says' + data.decode('utf-8')
            if not data:
                break
            else:
                sock.getpeername()
                while player==1:
                    count=0
                    while count<5:
                        player1ships.append(data)
                        ++count
                while player==2:
                    count=0
                    while count<5:
                        player2ships.append(data)
                        ++count
            print('locations: ')
            print(player1ships)
            print(player2ships)
            print('let the game begin')
            connection.sendall(str.encode(reply))
        connection.close()
    currentplayer=0
    while True:
        conn,addr = serv.accept()
        print('connected to ' + addr[0] + ':' + str(addr[1]))
        start_new_thread(threadclient,(conn,currentplayer))
        ThreadCount+=1
        currentplayer+=1
        print('threads: ' + str(ThreadCount))

    serv.close()
startserver()
