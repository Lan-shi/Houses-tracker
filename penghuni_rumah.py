#⁡⁢⁢⁣​‌‌‍C. Membuat fungsi untuk me return nama pemilik rumah atau tidak diketahui​

def penghuni_rumah(num,banyak_rumah,rumah_ganjil,rumah_genap) :
    #engkondisian jika nomor yg di input masih dibawah banyak nya rumah yg ada 
    if num < banyak_rumah+1 :
        if num % 2 == 0: # pengkondisian jika nomor yg di input berupa genap
            number = rumah_genap.get(num)
            return number
        else:# pengkondisian jika nomor yg di input berupa ganjil
            number = rumah_ganjil.get(num)
            return number
    #pengkondisian jika nomor yg di input melebihi banyaknya rumah
    else:
        return "tidak tahu"
