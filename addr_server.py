import socket
import addressing

server=socket.socket()
server.bind((socket.gethostname(),9994))
server.listen(5)
client,addr=server.accept()
subnet=client.recv(1024)
supernet=client.recv(1024)
print("Got message ",subnet.decode('utf-8'),supernet.decode('utf-8')," from ",addr[0])
try:
    subnet=int(subnet)
    supernet=int(supernet)
except:
    subnet=24
addressing.checkclass('192.168.43.208',subnet,supernet)
server.close()
