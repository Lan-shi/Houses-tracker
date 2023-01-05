# ​‌‌‍⁡⁢⁢⁣Fungsi tambahan yang saya buat untuk memudahkan memasukan data dari gosip tanpa melakukan ​
# ​‌‌‍looping yang memakan banyak tempat di main_program​

def cari_posisi(data_ke,rumah_ganjil,rumah_genap,gosip) :
    # membuat variable yang berisikan list dari key dan value 
    # yang berasal dari dict ganjil dan genap
    keys_ganjil=list(rumah_ganjil.keys())
    values_ganjil=list(rumah_ganjil.values())
    keys_genap=list(rumah_genap.keys())
    values_genap=list(rumah_genap.values())
    # variable untuk memudahkan penulisan code pada saat pengkondisian 
    # gosip[data][angka] merupakan data perbaris dari file teks 
    posisi = gosip[data_ke][2]
    arah = gosip[data_ke][3]
    nom = int(gosip[data_ke][0])
    pemilik = gosip[data_ke][9]
    petunjuk_rumah = gosip[data_ke][5]
    #pengkondisian jika paetunjuk rumah berada di value dictionary ganjil
    if petunjuk_rumah in values_ganjil:    
        idx_petunjuk_rumah = values_ganjil.index(petunjuk_rumah) # memunculkan index dari list value nya
        posisi_awal = keys_ganjil[idx_petunjuk_rumah] # menggunakan index diatas untuk mengambil keys dari list key
        #pengkondisian jika posisi berada di sebrang patokan(posisi_awal) 
        if posisi == "seberang" :             
            nomor_rumah = posisi_awal
            nomor_rumah += 1 #karena berada disebrang barisan ganjil, maka ditambah 1
            #pengkondisian kearah mana nomor_rumah bergerak dari posisi awal
            if arah == "kanan" : # kanan berarti menjadi lebih besar
                nomor_rumah += 2*nom
                #menentukan data nomor rumah masuk ke dictionary ganjil atau genap
                if nomor_rumah % 2 != 0 :
                    rumah_ganjil[nomor_rumah] = pemilik
                else:
                    rumah_genap[nomor_rumah] = pemilik
            elif arah == "kiri" : #kiri berarti menjadi lebih kecil
                nomor_rumah -= 2*nom
                #menentukan data nomor rumah masuk ke dictionary ganjil atau genap
                if nomor_rumah % 2 != 0 :
                    rumah_ganjil[nomor_rumah] = pemilik
                else:
                    rumah_genap[nomor_rumah] = pemilik
        # pengkondisian jika posisi berada di sebelah maka tidak perlu merubah posisi awal 
        elif posisi == "sebelah" :
            nomor_rumah = posisi_awal
            if arah == "kanan" : # kanan berarti menjadi lebih besar
                nomor_rumah += 2*nom
                #menentukan data nomor rumah masuk ke dictionary ganjil atau genap
                if nomor_rumah % 2 != 0 :
                    rumah_ganjil[nomor_rumah] = pemilik
                else:
                    rumah_genap[nomor_rumah] = pemilik
            elif arah == "kiri" : # kiri berarti menjadi lebih kecil
                nomor_rumah -= 2*nom
                #menentukan data nomor rumah masuk ke dictionary ganjil atau genap
                if nomor_rumah % 2 != 0 :
                    rumah_ganjil[nomor_rumah] = pemilik
                else:
                    rumah_genap[nomor_rumah] = pemilik
    #pengkondisian jika petunjuk rumah berada di value dictionary genap
    elif petunjuk_rumah in values_genap:
        idx_petunjuk_rumah = values_genap.index(petunjuk_rumah) # memunculkan index dari list value nya
        posisi_awal = keys_genap[idx_petunjuk_rumah] # menggunakan index diatas untuk mengambil keys dari list key
        #pengkondisian jika posisi berada di sebrang patokan(posisi_awal) 
        if posisi == "seberang" :
            nomor_rumah = posisi_awal
            nomor_rumah -= 1 #karena berada disebrang barisan genap, maka dikurang 1
            if arah == "kanan" : # kanan berarti menjadi lebih besar
                nomor_rumah += 2*nom
                #menentukan data nomor rumah masuk ke dictionary ganjil atau genap
                if nomor_rumah % 2 != 0 :
                    rumah_ganjil[nomor_rumah] = pemilik
                else:
                    rumah_genap[nomor_rumah] = pemilik                
            elif arah == "kiri" : #kiri berarti menjadi lebih kecil
                nomor_rumah -= 2*nom
                #menentukan data nomor rumah masuk ke dictionary ganjil atau genap
                if nomor_rumah % 2 != 0 :
                    rumah_ganjil[nomor_rumah] = pemilik
                else:
                    rumah_genap[nomor_rumah] = pemilik    
        elif posisi == "sebelah" :
            nomor_rumah = posisi_awal
            if arah == "kanan" : # kanan berarti menjadi lebih besar
                nomor_rumah += 2*nom
                #menentukan data nomor rumah masuk ke dictionary ganjil atau genap
                if nomor_rumah % 2 != 0 :
                    rumah_ganjil[nomor_rumah] = pemilik
                else:
                    rumah_genap[nomor_rumah] = pemilik                 
            elif arah == "kiri" : #kiri berarti menjadi lebih kecil
                nomor_rumah -= 2*nom
                #menentukan data nomor rumah masuk ke dictionary ganjil atau genap
                if nomor_rumah % 2 != 0 :
                    rumah_ganjil[nomor_rumah] = pemilik
                else:
                    rumah_genap[nomor_rumah] = pemilik   