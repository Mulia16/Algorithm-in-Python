import socket
import threading
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
IP, PORT = ("127.0.0.1", 8080)
s.bind((IP, PORT))
print(f"Mendegarkan {IP}:{PORT}")
def clientConn() :
    message, addr = s.recvfrom(1024)
    print(f"IP Client {addr[0]}:{addr[1]}")
    print("Pesan Client :", message.decode("utf-8"))
    s.sendto("Saya Server UDP".encode("utf-8"), addr)
while True :
    threading.Thread(target=clientConn).start()
s.close()