from time import sleep as wait
List = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",]
def coreLoop(jumlah, batas) :
    global hasil
    global nilaiIden
    if batas < jumlah :
        for i in List :
            identitas = batas
            nilaiIden.insert(identitas - 1, i)
            hasil["res"] = nilaiIden[:identitas]
            coreLoop(jumlah, batas + 1)
    elif batas == jumlah :
        for i in List :
            identitas = batas
            nilaiIden.insert(identitas - 1, i)
            hasil["res"] = nilaiIden[:identitas]
            hasilAkhir = ""
            for i in hasil["res"] :
                hasilAkhir += i
            print(hasilAkhir)
            wait(1)
jumlah = 0
while True :
    hasil = {"res":""}
    jumlah +=1
    nilaiIden = []
    coreLoop(jumlah, 1)