import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',5050))
num1="2222"
num2="1111"
client.send(num1.encode('utf-8'))
client.send(num2.encode('utf-8'))
from_server = (client.recv(4096)).decode('utf-8')
client.close()
print('server message: ',from_server)
