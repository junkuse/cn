import socket

server=socket.socket()
server.connect((socket.gethostbyname(socket.gethostname()),9994))
msg=str(input("Kindly enter your initial network mask:- "))
server.send(msg.encode('utf-8'))
msg=str(input("Kindly enter your final network mask:- "))
server.send(msg.encode('utf-8'))
server.close()