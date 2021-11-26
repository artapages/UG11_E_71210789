# menu
print("Menu Program Yang Tersedia")
print("1. pangkatkan angka")
print("2. akarkan bilangan")
pilihan = int(input("Masukkan pilihan yang diinginkan : "))

#proses
def pangkatAngka (pilihan):
    print("Masukkan angka yang ingin di Pangkatkan")
    angka = float(input("Angka : "))
    print("ingin memodifikasi pangkat ?(yes/no)")
    modifikasi = input(": ")
    if modifikasi == "yes":
        nilai = float(input("Masukkan nilai pangkat : "))
        penyelesaian = float ( angka ** nilai )
        print("Hasil dari ", angka, "^", nilai, "=", penyelesaian)
    elif modifikasi == "no" :
        penyelesaian2 = float( angka ** 2 )
        print("Hasil dari ", angka, "^ 2 = ", penyelesaian2)

def akarBilangan (pilihan):
    print("Masukkan angka yang ingin di akar")
    angka = float(input("Angka : "))
    print("ingin memodifikasi pangkat ?(yes/no)")
    modifikasi = input(": ")
    if modifikasi == "yes":
        nilai = float(input("Masukkan nilai akar : "))
        penyelesaian = float ( angka ** ( 1 / nilai ) ) 
        print("Hasil akar pangkat ", nilai, "dari", angka, "=", penyelesaian)
    elif modifikasi == "no" :
        penyelesaian2 = float ( round ( angka ** ( 1 / 2), 2) )
        print("Hasil akar pangkat ", pilihan, "dari", angka, "=", penyelesaian2)

if pilihan == 1:
    pangkatAngka (pilihan)
else :
    akarBilangan (pilihan)
