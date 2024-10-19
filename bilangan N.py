def terbesar_dari_N():
    bilangan_terbesar = None
    
    while True:
        n = int(input("Masukkan bilangan (masukkan 0 untuk berhenti): "))
        
        if n == 0:
            break
        
        if bilangan_terbesar is None or n > bilangan_terbesar:
            bilangan_terbesar = n
    
    return bilangan_terbesar

hasil = terbesar_dari_N()
if hasil is not None:
    print("Bilangan terbesar adalah:", hasil)
else:
    print("Tidak ada bilangan yang dimasukkan.")
