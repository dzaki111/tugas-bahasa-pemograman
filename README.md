# tugas-bahasa-pemograman-ke-5

### Nama   = DZAKI ARIF RAHMAN  
### Kelas  = TI.24.A4  
### NIM    = 312410312  
### Matkul = BAHASA PEMOGRAMAN

# Menentukan Bilangan Terbesar dari Serangkaian Input

Program ini digunakan untuk mencari bilangan terbesar dari sekumpulan bilangan yang dimasukkan oleh pengguna. Proses penginputan bilangan akan terus berlanjut hingga pengguna memasukkan angka 0, yang menandakan bahwa input telah selesai. Setelah itu, program akan menampilkan bilangan terbesar dari sekumpulan bilangan yang sudah dimasukkan.

## Deskripsi Program

Program ini meminta pengguna untuk memasukkan bilangan secara berulang. Pengguna dapat terus memasukkan bilangan sampai mereka memasukkan angka `0`, yang menjadi tanda berhenti untuk program. Setiap kali bilangan baru dimasukkan, program akan mengecek apakah bilangan tersebut lebih besar dari bilangan terbesar sebelumnya. Jika iya, maka bilangan tersebut disimpan sebagai bilangan terbesar.

Jika pengguna tidak memasukkan bilangan apapun dan langsung memasukkan `0`, program akan menampilkan pesan bahwa tidak ada bilangan yang dimasukkan.

### Fitur Utama:
- Program menerima serangkaian input bilangan.
- Program secara otomatis menentukan bilangan terbesar dari input tersebut.
- Program berhenti menerima input ketika pengguna memasukkan angka `0`.

## Kode Program

```python
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
```
# Hasil screenshot di visualstudiocode

![Screenshot 2024-10-19 201145](https://github.com/user-attachments/assets/365486ac-4cba-4d83-baa3-6aed0b76d806)

# Berikut adalah flowchartnya

![Screenshot 2024-10-19 202141](https://github.com/user-attachments/assets/ca02747f-5475-44eb-b64d-b6ec6a84a416)


## Penjelasan Kode

1. **Inisialisasi Variabel:**
   - `bilangan_terbesar` diinisialisasi sebagai `None` untuk menyimpan bilangan terbesar yang ditemukan.
   
2. **Pengulangan (Loop):**
   - Program menggunakan loop `while True` untuk menerima input bilangan dari pengguna.
   - Setiap kali pengguna memasukkan bilangan, program memeriksa apakah bilangan tersebut adalah `0`. Jika iya, loop berhenti dengan perintah `break`.
   
3. **Penentuan Bilangan Terbesar:**
   - Jika `bilangan_terbesar` masih `None` (artinya belum ada bilangan yang disimpan) atau jika bilangan yang baru dimasukkan lebih besar dari `bilangan_terbesar` saat ini, maka `bilangan_terbesar` akan diperbarui dengan bilangan tersebut.
   
4. **Hasil Akhir:**
   - Setelah loop berakhir, program mengecek apakah ada bilangan yang dimasukkan (bilangan terbesar tidak `None`).
   - Jika ada bilangan yang dimasukkan, program akan menampilkan bilangan terbesar tersebut.
   - Jika tidak ada bilangan yang dimasukkan (langsung `0` tanpa input bilangan lain), program akan menampilkan pesan bahwa tidak ada bilangan yang dimasukkan.

## Contoh Eksekusi Program

### Contoh 1:
Pengguna memasukkan beberapa bilangan sebelum berhenti dengan `0`.

```
Masukkan bilangan (masukkan 0 untuk berhenti): 12
Masukkan bilangan (masukkan 0 untuk berhenti): 45
Masukkan bilangan (masukkan 0 untuk berhenti): 22
Masukkan bilangan (masukkan 0 untuk berhenti): 0
Bilangan terbesar adalah: 45
```

### Contoh 2:
Pengguna langsung memasukkan `0` tanpa memasukkan bilangan lainnya.

```
Masukkan bilangan (masukkan 0 untuk berhenti): 0
Tidak ada bilangan yang dimasukkan.
```

## Cara Menjalankan Program

1. Pastikan kamu memiliki Python terinstall di komputer kamu.
2. Simpan kode program ke dalam file Python, misalnya `menentukan_bilangan_terbesar.py`.
3. Jalankan program melalui terminal atau command prompt:
    ```bash
    python3 menentukan_bilangan_terbesar.py
    ```
4. Masukkan bilangan secara berurutan. Ketik `0` ketika ingin menghentikan input.
5. Program akan menampilkan bilangan terbesar atau pesan jika tidak ada bilangan yang dimasukkan.

# menetukan 3 bilangan terbesar

Program ini digunakan untuk menemukan bilangan terbesar dari tiga bilangan yang dimasukkan oleh pengguna. Program meminta tiga bilangan sebagai input, membandingkannya, dan kemudian mencetak bilangan terbesar di antara ketiga bilangan tersebut.

## Kode Program

```python
a = int(input('Masukkan bilangan pertama: '))
b = int(input('Masukkan bilangan kedua: '))
c = int(input('Masukkan bilangan ketiga: '))

if a > b and a > c:
    print(f'Bilangan terbesar adalah {a}')
elif b > a and b > c:
    print(f'Bilangan terbesar adalah {b}')
else:
    print(f'Bilangan terbesar adalah {c}')
```

# Hasil screenshot di visualstudiocode

![Screenshot 2024-10-19 201145](https://github.com/user-attachments/assets/f01f9fce-7b67-4b2e-b63a-cb613ee4b9ae)

# Berikut adalah flowchartnya

![Screenshot 2024-10-20 162920](https://github.com/user-attachments/assets/5ca9a3a9-5ea6-428d-b7df-f3e82bcc4003)

## Penjelasan Kode

1. **Input Bilangan:**
   Program meminta pengguna memasukkan tiga bilangan menggunakan fungsi `input()` dan mengonversinya menjadi bilangan bulat (`int`), kemudian disimpan ke variabel `a`, `b`, dan `c`.

2. **Logika Penentuan Bilangan Terbesar:**
   - Program menggunakan struktur kondisi `if-elif-else` untuk membandingkan ketiga bilangan.
   - Jika `a` lebih besar dari `b` dan `c`, program akan mencetak bahwa `a` adalah bilangan terbesar.
   - Jika `b` lebih besar dari `a` dan `c`, program akan mencetak bahwa `b` adalah bilangan terbesar.
   - Jika tidak ada kondisi di atas yang terpenuhi, program akan menganggap bahwa `c` adalah bilangan terbesar dan mencetaknya.

3. **Output:**
   Program akan mencetak bilangan terbesar yang ditemukan di antara ketiga bilangan yang diinputkan oleh pengguna.

## Contoh Eksekusi Program

### Contoh 1:
Pengguna memasukkan tiga bilangan, yaitu `10`, `20`, dan `15`.

```
Masukkan bilangan pertama: 10
Masukkan bilangan kedua: 20
Masukkan bilangan ketiga: 15
Bilangan terbesar adalah 20
```

### Contoh 2:
Pengguna memasukkan tiga bilangan, yaitu `45`, `35`, dan `50`.

```
Masukkan bilangan pertama: 45
Masukkan bilangan kedua: 35
Masukkan bilangan ketiga: 50
Bilangan terbesar adalah 50
```
# PRAKTIKUM 3 LATIHAN 1

<img width="712" alt="image" src="https://github.com/user-attachments/assets/1447f1ff-cdc7-42cd-a86c-90956cac26f5">

## PENGGUNAAN END
<img width="286" alt="image" src="https://github.com/user-attachments/assets/6d7f5c02-fa7a-46bf-97b4-1bf8f3a45e90">

python
print('A', end='')
print('b', end='')
print('c', end='')
print()
print('x')
print('y')
print('z')
`

Parameter end dalam fungsi Print () di python di gunakan untuk menambahkan string(" ")apapun diakhir dan mengeluarkan pertanyaan print

python
print()
`

Secara default,fungsi print() akan mengakhiri dengan baris baru,dan akan secara otomatis karakter baris baru di akhir outputnya

inilah hasil program tersebut:

![Screenshot 2024-10-19 105401](https://github.com/user-attachments/assets/e4be0ae6-0c1e-46ab-a947-1470668b5387)

dan ini hasil tanpa menggunakan fungsi print() di tengah pada kode program di atas:

![Screenshot 2024-10-19 105727](https://github.com/user-attachments/assets/ce8c4426-642e-4460-b59e-31b88d4bd59b)

## PENGGUNAAN SEREPATOR

![Screenshot 2024-10-19 105946](https://github.com/user-attachments/assets/f883e3f9-751b-4be6-973a-a1720cf8d062)

```python
w, x, y, z, =10, 15, 20, 25
print(w, x, y, z,)
print(w, x, y, z, sep=',')
print(w, x, y, z, sep='')
print(w, x, y, z, sep=':')
print(w, x, y, z, sep='-----')
```
pada python penggunaan serepator dapat menggunakan fungsi split() atau sep yang seperti dalam kode program di atas

serepator ini menentukan pembatasan yang digunakan untuk memisahkan sting,serepator dapat berupa karakter tunggal atau beberapa karakter.jika tidak ditentukan,maka python akan menggunakan spasi sebagai pemisah.

Berikut Hasil Kode Program Diatas:

![Screenshot 2024-10-19 111502](https://github.com/user-attachments/assets/9afa0286-fcd8-437e-8319-0da6019ef34e)

```python
w, x, y, z, =10, 15, 20, 25
```
Variable yang seperti ini menentukan parameter,jadi variable ini tidak bisa memasukan variable angka yang sudah ditentukan w = 10,x=15,y=20,z=25

```python
print(w, x, y, z,)
```

Fungsi ini hanya mencetak saja yang menggunakan fungsi print(), tetapi di karenakan mencetak parameter,koma tersebut di hilangkan

```python
print(w, x, y, z, sep=',')
```
karena pemisahnya dihilangkan,kita menggunakan fungsi `sep`atau`split()`dan kita memasukkan pemisahnya didalam string akan memunculkan cetakan yang sesuai keinginan anda dalam memisahkan sesuatu parameter

## STRING FORMAT

![Screenshot 2024-10-19 112724](https://github.com/user-attachments/assets/d5f2d127-76c0-4653-996c-aa5e6d201274)

```python
print(0, 10**0)
print(1, 10**1)
print(2, 10**2)
print(3, 10**3)
print(4, 10**4)
print(5, 10**5)
print(6, 10**6)
print(7, 10**7)
print(8, 10**8)
print(9, 10**9)
print(10, 10**10)

print('{0:>3} {1:>16}'.format(0, 10**0))
print('{0:>3} {1:>16}'.format(1, 10**1))
print('{0:>3} {1:>16}'.format(2, 10**2))
print('{0:>3} {1:>16}'.format(3, 10**3))
print('{0:>3} {1:>16}'.format(4, 10**4))
print('{0:>3} {1:>16}'.format(5, 10**5))
print('{0:>3} {1:>16}'.format(6, 10**6))
print('{0:>3} {1:>16}'.format(7, 10**7))
print('{0:>3} {1:>16}'.format(8, 10**8))
print('{0:>3} {1:>16}'.format(9, 10**9))
print('{0:>3} {1:>16}'.format(10, 10**10))
```
String Format adalah proses memasukan variable atau string kustom ke dalam teks yang sudah ditentukan,dan dapat digunakan untuk berbagai keperluan,seperti memasukan judul dalam grafik,menampilkan pesan atau kesalahan, atau meneruskan kesalahan ke suatu fungsi 

```python
print(0, 10**0)
print(1, 10**1)
print(2, 10**2)
print(3, 10**3)
print(4, 10**4)
print(5, 10**5)
print(6, 10**5)
print(8, 10**8)
print(9, 10**9)
print(10, 10**10)
```

Nilai pertama dalam setiap pasangan adalah angka dari 0 hingga 10, kode program ini dihitung dengan menggunakan operasi pangkat atau fungsinya (**) untuk menaikkan 10 ke pangkat yang sesuai dengan angka pertama, yang bisa di bahasa manusiakan variable 0 = 10 pangkat 0, variable 1 10 pangkat 1 dan seterusnya hingga variable 10 yaitu 10 pangkat 10, dan di cetak dengan fungsi print()

```python
print('{0:>3} {1:>16}'.format(0, 10**0))
print('{0:>3} {1:>16}'.format(1, 10**1))
print('{0:>3} {1:>16}'.format(2, 10**2))
print('{0:>3} {1:>16}'.format(3, 10**3))
print('{0:>3} {1:>16}'.format(4, 10**4))
print('{0:>3} {1:>16}'.format(5, 10**5))
print('{0:>3} {1:>16}'.format(6, 10**6))
print('{0:>3} {1:>16}'.format(7, 10**7))
print('{0:>3} {1:>16}'.format(8, 10**8))
print('{0:>3} {1:>16}'.format(9, 10**9))
print('{0:>3} {1:>16}'.format(10, 10**10))
```

Kode ini mencetak 11 baris dengan format {0:3} {1:16} yang di gunakan untuk mengatur format string

Pada string pertama, angka 0 di format untuk memeliki lebar 3 karakter atau yang bisa disebut 3 kali spasi dengan perataan kanan.

angka 1 diformat untuk memiliki lebar 16 Karakter atau 16 kali spasi dengan perataan kanan, dan masing-masing mencetak nilai seperti format di atas dengan fungsi print()
