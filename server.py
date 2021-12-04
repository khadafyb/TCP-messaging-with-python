import socket
serv=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serv.bind(('127.0.0.1',5050))
serv.listen(5)
while True:
    conn,addr = serv.accept()
    from_client = ' '
    result=0
    n=''
    listn=[]
    while True:
        data = conn.recv(4096)
        if not data:break
        from_client += data.decode('utf-8')

        str(data)
        for i in from_client:
            if(i.isdigit() and not i.isspace() ):
                result=result+int(i)
        print('client sent: ',from_client)
    
        result=str(result)
        message='hello client! sum = '+result
        conn.send(message.encode('utf-8'))
    conn.close()
    print('client closed')
