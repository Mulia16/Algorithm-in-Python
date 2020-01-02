import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True :
    s.sendto("Saya client UDP".encode("utf-8"), ("192.168.43.173", 8080))
    message, addr = s.recvfrom(1024)
    print("Pesan server:", message.decode("utf-8"))
    print(f"IP Server {addr[0]}:{addr[1]}")
s.close()