import socket
client=socket.socket()
host = '127.0.0.1'
port = 1233
print('waiting for connection')
try:
    client.connect((host,port))
except socket.error as e:
    print(str(e))
response = client.recv(1024)
while True:
    inp=input("enter coordinates: ")
    client.send(str.encode(inp))
    response = client.recv(1024)
    print(response.decode('utf-8'))
client.close()
