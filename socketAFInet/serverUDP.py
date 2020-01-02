import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
IP, PORT = ("0.0.0.0", 8080)
s.bind((IP, PORT))
print(f"Mendegarkan {IP}:{PORT}")
while True :
    message, addr = s.recvfrom(1024)
    print(f"IP Client {addr[0]}:{addr[1]}")
    print("Pesan Client :", message.decode("utf-8"))
    s.sendto("Saya Server UDP".encode("utf-8"), addr)
s.close()