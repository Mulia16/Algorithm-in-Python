import socket
import os
print("Menghubungkan...")
if os.path.exists("/programming/python/socketAFUnix/socketUnix.s"):
    client = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    client.connect("/programming/python/socketAFUnix/socketUnix.s")
    while True:
        try:
            x = input("> ")
            if "" != x:
                print("Kirim :", x)
                client.send(x.encode('utf-8'))
                if "DONE" == x:
                    print("Shutting down.")
                    break
        except KeyboardInterrupt as k:
            client.close()
            break
else:
    print("Tidak terhubung!")