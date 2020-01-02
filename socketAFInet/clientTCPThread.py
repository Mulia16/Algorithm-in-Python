import socket
import threading
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 10000))
s.connect(("127.0.0.1", 8888))
def inputTCP(s) :
    while True :
        pesan = input("")
        pesan = "exit" if pesan == "" else pesan
        s.send(pesan.encode("utf-8"))
        if pesan == "exit" :
            s.close()

def outputTCP(s) :
    while True :
        print("\nPesan server :", s.recv(1024).decode("utf-8"))

threading.Thread(target=inputTCP, args=(s,)).start()
threading.Thread(target=outputTCP, args=(s,)).start()