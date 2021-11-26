# Awalan
word = input("Masukkan kata : ")

#proses
def Kata_Tengah(word) :
    edit = len ( word )
    if edit % 2 == 0 :
        if edit < 8 :
            x = int ( edit / 2 )
            Penyelesaian = word [ x - 1 ] + word [ x ]
            return Penyelesaian
        else:
            x = int ( edit / 2 )
            Penyelesaian = word [ x - 2 ] + word [ x - 1 ] + word [ x ] + word [ x + 1 ]
            return Penyelesaian
    elif  edit % 2 == 1 :
        if edit < 5 :
            x = int ( ( edit - 1 ) / 2 )
            Penyelesaian = word [ x ]
            return Penyelesaian
        elif edit >= 5 :
            x = int ( ( edit - 1 ) / 2 )
            Penyelesaian = word [ x - 1 ] + word [ x ] + word [ x + 1 ]
            return Penyelesaian
print ("Huruf tengah pada kata", word,"adalah", Kata_Tengah(word) )