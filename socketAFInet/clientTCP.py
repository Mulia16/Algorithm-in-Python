import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 10000))
s.connect(("10.10.4.75", 2112))
while True :
    s.send("Saya Server TCP".encode("utf-8"))
    print(s.recv(1024).decode("utf-8"))
s.close()
