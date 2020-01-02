import socket
import threading
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 8888))
s.listen(5)
print("Mendegarkan 0.0.0.0:8888")
def inputTCP(client):
    while True :
        pesan = input("")
        pesan = "exit" if pesan == "" else pesan
        client.send(pesan.encode("utf-8"))
        if pesan == "exit" :
            client.close()
            s.close()
            break

def outputTCP(client) :
    while True :
        print("\nPesan Client :", client.recv(1024).decode("utf-8"))

client, addr = s.accept()
print("IP Client {0}:{1}".format(addr[0], addr[1]))
threading.Thread(target=inputTCP, args=(client,)).start()
threading.Thread(target=outputTCP, args=(client,)).start()