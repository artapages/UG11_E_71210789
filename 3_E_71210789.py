# menu
print("=======Program Manipulasi String=======")
print("Pilihan Menu : ")
print ("1. Hitung kata ")
print ("2. cek kata ")
print ("3. ubah kata ")

pilihan = input("Pilihan anda : ")

# Pilihan 1
def Hitung_kata() :
    kalimat = input ("Masukkan sebuah kalimat/kata : ")
    hitungan = input ("Masukkan kata yang ingin dihitung : ")
    penykal = kalimat.lower()
    penyhit = hitungan.lower()
    if penyhit in penykal :
        x = penykal.count ( penyhit )
        print ("Terdapat sebanyak", x,"kata", hitungan,"di dalam string" )

# Pilihan 2
def cek_kata():
    kalimat = input ("Masukkan sebuah kalimat/kata : ")
    cek = input ("Masukkan kata yang ingin di cek : ")
    if cek in kalimat :
        print ("Kata", cek,"terdapat di dalam string")
        print ("String diubah menjadi : ")
        x = kalimat.replace ( cek, cek.upper() )
        print (x)
    else :
        print ("Kata", cek, "tidak terdapat di dalam string ")
        print ("String diubah menjadi : ")
        print ( kalimat , cek )

# Pilihan 3
def ubah_kata() :
    kalimat = input ("Masukkan sebuah kalimat/kata : ")
    ubah = input ("Masukkan kata yang ingin di ubah : ")
    pengganti= input ("Masukkan kata pengganti : ")
    print ("Anda akan mengubah kata", ubah, "menjadi", pengganti, "sebanyak 1x")
    total = input ("Apakah anda ingin mengubah jumlah total penggantian kata ? (yes/no) : ")
    if total == "yes" :
        jumlah = int ( input ("Masukkan jumlah total penggantian : ") )
        print ("String berhasil diubah menjadi : ")
        print ( kalimat.replace ( ubah, pengganti, jumlah) )
    elif total == "no" :
        print ("String berhasil diubah menjadi : ")
        print ( kalimat.replace ( ubah, pengganti, 1) )

if pilihan  == "1" :
    Hitung_kata()
elif pilihan == "2" :
    cek_kata()
elif pilihan == "3" : 
    ubah_kata()
else :
    print("Pilihlah yang ada dimenu!")