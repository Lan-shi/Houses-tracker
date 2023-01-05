""""
⁡⁢⁣⁣​‌‌‍𝔸𝕙𝕞𝕒𝕕 𝕄𝕒𝕦𝕝𝕒𝕟𝕒 𝕀𝕟𝕕𝕚𝕕𝕙𝕒𝕣𝕞𝕒𝕟𝕥𝕠 
𝟙𝟛𝟘𝟙𝟚𝟙𝟘𝟛𝟡𝟘
𝕀𝔽𝟜𝟝𝟘𝟞⁡⁡​
"""

#Mempersiapkan dictionary dan list kosong untuk dimasukan ke data dari file teks yg akan di open
rumah_ganjil={}
rumah_genap={}
data=[]

#mengakses teks file dan memasukan ke list data
# saya menggunakan path untuk open nya karena kalo pake langsung nama filenya
# gatau kenapa ga bisa di akses
file=open("A:\Telyu\peng_pro\TUBES_2021_1301210390_Ahmad Maulana Indidharmanto/teks.txt","r")
for i in file:
    data.append(i.split()) #memasukan isi file yg dibuka kedalam data sekaligus di split per baris dan kata
listdata = list(map(int,data[0])) #mengisolasi baris 1 agar memudahkan pengaksesan data
#men-split list berdasar index untuk memudahkan
nomor_rumah_anda = listdata[0]
banyak_rumah = listdata[1]
banyak_gosip = len(data[1:])
gosip = data[1:]
file.close()

# ​‌‌‍A.membuat dictionary ganjil dan genap dan mengisikan data seadanya terlebih dahulu
x=1 #inisialisasi 
while x in range (1,banyak_rumah+1) : # x dari 1 sampai yg batas terakhir
    if x % 2 == 0 : #memisahkan untuk yg genap
        rumah_genap[x] = "tidak tahu"
        x +=1
    else:   # memisahkan untuk yg ganjil
        rumah_ganjil[x] = "tidak tahu"
        x +=1             
# karena dari data[1][1] value nya menunjukan rumah milik anda
# maka di masukkan ke dictionary sesuai dengan key nya yg berupa nomor rumah
if nomor_rumah_anda % 2 == 0:
    rumah_genap[nomor_rumah_anda] = "anda" #memisahkan jika genap
else:
    rumah_ganjil[nomor_rumah_anda] = "anda"#memisahkan jika ganjil


# ​‌‍‌​‌‌‍𝗠𝗮𝗶𝗻 𝗣𝗿𝗼𝗴𝗿𝗮𝗺​​
# Menampilkan dictionary dan memanggil fungsi yang dibuat
from cari_posisi import cari_posisi #fungsi yang telah dibuat untuk memasukan nomor dan pemilik rumah berdasar gosip ke dictionary
from nomor_rumah import nomor_rumah #fungsi yang telah dibuat untuk mencari nomor rumah
from penghuni_rumah import penghuni_rumah #fungsi yang telah dibuat untuk mencari pemilik rumah 
j=0 #inisialisasi
#mengulang kondisi selama j tidak melebih gosip yg didapat
while j < banyak_gosip : 
    cari_posisi(j,rumah_ganjil,rumah_genap,gosip)
    j= j + 1

# menampilkan dictionary 
print("dictionary genap :\n",rumah_genap)
print("dictionary ganjil :\n",rumah_ganjil)
#memilih ingin memanggil fungsi apa
dict_fungsi = {1:"Nomor Rumah",2:"Penghuni Rumah"}
for a,f in dict_fungsi.items():
    print(a,f)
print ("Silahkan Pilih Ingin Mencari Apa")
pilihan =int(input())
if pilihan == 1:
    #memanggil fungsi pencari nomor rumah
    nama = input("Masukkan Nama Pemilik Rumah: ")
    panggil_nomor = nomor_rumah(nama,rumah_ganjil,rumah_genap)
    if panggil_nomor != "tidak tahu" :
        print("Nomor rumah dari",nama,"adalah",panggil_nomor)
    else:
        print("Nomor rumah dari",nama,"tidak diketahui")
elif pilihan == 2:
    #memanggil fungsi pencari penghuni rumah
    print("Masukkan Nomor Rumah:")
    nom = int(input())
    panggil_penghuni = penghuni_rumah(nom,banyak_rumah,rumah_ganjil,rumah_genap)
    if panggil_penghuni != "tidak tahu":
        print("Pemilik rumah dari",nom,"adalah",panggil_penghuni)
    else:
        print("Pemilik rumah dari nomor rumah",nom,"tidak diketahui")

