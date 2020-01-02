from ftplib import FTP
ftp = FTP()
host = input("Masukkan host FTP Server : ")
port = input("Masukkan port FTP Server (21) : ")
port = 21 if port == "" else int(port)
print(ftp.connect(host, port)[4::])
username = input("Masukkan username : ")
password = input("Masukkan password : ")
ftp.login(username, password)
print("Berhasil login...\n")

def uploadFile(file):
    ftp.storbinary('STOR ' + file, open(lokasi + file, 'rb'))
    print("upload berhasil...")

def downloadFile(file, lokasi):
    localfile = open(lokasi + file, 'wb')
    ftp.retrbinary('RETR ' + file, localfile.write)
    localfile.close()
    print("download berhasil...")

while True :
    print("perintah :\n- list\n- cwd\n- upload\n- download\n- exit")
    cmd = input("Masukkan perintah : ")
    if cmd.lower() == "list" :
        print(ftp.retrlines("LIST"))
    elif cmd.lower() == "cwd" :
        direct = input("Masukkan perintah : ")
        ftp.cwd(direct)
    elif cmd.lower() == "upload" :
        file = input("Masukkan nama file beserta extensinya : ")
        lokasi = input("Masukkan lokasi penyimpanan : ")
        uploadFile(file, lokasi)
    elif cmd.lower() == "download" :
        file = input("Masukkan nama file beserta extensinya : ")
        lokasi = input("Masukkan lokasi penyimpanan :")
        downloadFile(file, lokasi)
    elif cmd.lower() == "cmd" :
        print(ftp.sendcmd("LIST"))
    elif cmd.lower() == "exit" :
        ftp.quit()
        break
    print(30 * "=" )