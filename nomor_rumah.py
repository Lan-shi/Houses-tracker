# ​‌‌‍⁡⁢⁢⁣B. Membuat fungsi yang mereturn nomor rumah atau tidak diketahui​

def nomor_rumah(nama,rumah_ganjil,rumah_genap):
    # membuat variable yang berisikan list dari key dan value 
    # yang berasal dari dict ganjil dan genap
    keys_ganjil=list(rumah_ganjil.keys())
    values_ganjil=list(rumah_ganjil.values())
    keys_genap=list(rumah_genap.keys())
    values_genap=list(rumah_genap.values())
    # Pengkondisian jika nama yang di input berada di list value dictionary ganjil
    if nama in values_ganjil:
        idx =values_ganjil.index(nama)
        # me-return index dari list keys dictionary ganjil
        return keys_ganjil[idx]
    # Pengkondisian jika nama yang di input berada di list value dictionary genap
    elif nama in values_genap:
        idx = values_genap.index(nama)
        # me-return index dari list keys dictionary genap
        return keys_genap[idx]
    # jika nama yang dimasukan tidak terdata
    else :
        return "tidak tahu"