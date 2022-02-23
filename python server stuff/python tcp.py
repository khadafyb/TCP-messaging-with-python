import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1',5005))
sock.send("hello world")
sock.recv(4096)
sock.close()
