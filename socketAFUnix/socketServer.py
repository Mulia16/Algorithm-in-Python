import socket
import os
if os.path.exists("/programming/python/socketAFUnix/socketUnix.s"):
    os.remove("/programming/python/socketAFUnix/socketUnix.s")
server = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server.bind("/programming/python/socketAFUnix/socketUnix.s")
print("Mendengarkan...")
while True:
    datagram = server.recv(1024)
    if not datagram:
        break
    else:
        print(datagram.decode('utf-8'))
        if "EXIT" == datagram.decode('utf-8'):
            break
server.close()
os.remove("/programming/python/socketAFUnix/socketUnix.s")