import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP, PORT = ("0.0.0.0", 8888)
s.bind((IP, PORT))
print("Mendengarkan {0}:{1}".format(IP,PORT))
s.listen(5)
while True :
    client, addr = s.accept()
    print("IP Client {0}:{1}".format(addr[0], addr[1]))
    client.send("Saya server TCP".encode("utf-8"))
    print(client.recv(2048).decode("utf-8"))
    client.close()
s.close()

