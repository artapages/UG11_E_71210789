# level
import random
print("=======Program test aritmatika dasar=======")
print("Pilihan level yang tersedia : ")
print("1. Easy ")
print("2. Medium ")
print("3. Hard ")

#proses
def generate ( level ) :
    level = input("Masukkan tingkatan yang ingin anda coba : ")
    if level == "1" :
        pil1 = random.randint (20,50)
        pil2 = random.randint (20,50)
        carahitung = [ '+' ,'-' ,'/' ,'*' ]
        peny = random.choice ( carahitung )
        ditanya = str ( pil1 ) + str ( peny ) + str ( pil2 ) 
        print ("Berapakah hasil dari", ditanya)
        jawab = float(input("Maskkan Jawaban Anda : "))
        if jawab == round ( eval ( ditanya ), 3 ) :
            print("Jawaban Anda Benar !")
        else:
            print("Jawaban Anda Masih Salah !")
        return round ( eval ( ditanya ), 3 ), ditanya

    elif level == "2" :
        pil1 = random.randint (20,70)
        pil2 = random.randint (20,70)
        pil3 = random.randint (20,70)
        carahitung = ['+' ,'-' ,'/' ,'*']
        peny1 = random.choice ( carahitung )
        peny2 = random.choice ( carahitung )
        ditanya = str ( pil1 ) + str ( peny1 ) + str ( pil2 ) + str ( peny2 ) + str ( pil3 ) 
        print("Berapakah hasil dari", ditanya)
        jawab = float ( input ("Masukan Jawaban Anda : ") )
        if jawab == round ( eval ( ditanya ), 3 ) :
            print ("Jawaban Anda Benar ! ")
        else:
            print ("Jawaban Anda Masih Salah !")
        return round ( eval ( ditanya ), 3), ditanya
    
    elif level == "3" :
        pil1 = random.randint (20,100)
        pil2 = random.randint (20,100)
        pil3 = random.randint (20,100)
        pil4 = random.randint (20,100)
        carahitung = ['+' ,'-' ,'/' ,'*']
        peny1 = random.choice ( carahitung )
        peny2 = random.choice ( carahitung )
        peny3 = random.choice ( carahitung )
        ditanya = str ( pil1 ) + str ( peny1 ) + str ( pil2 ) + str ( peny2 ) + str ( pil3 ) + str ( peny3 ) + str ( pil4)
        print ("Berapakah hasil dari", ditanya, "?")
        jawab = float ( input ("Masukan Jawaban Anda : ") )
        if jawab == round ( eval ( ditanya ), 3 ) :
            print ("Jawaban Anda Benar ! ")
        else:
            print ("Jawaban Anda Masih Salah !")
        return round ( eval ( ditanya ), 3 ), ditanya

def cek_tingkatan ():
    peny1,peny2 = generate( level = input )
    print ("Hasil dari", peny2, "=", peny1 )

cek_tingkatan ()