# tugas-bahasa-pemograman-ke-5

Nama   = DZAKI ARIF RAHMAN  
Kelas  = TI.24.A4  
NIM    = 312410312  
Matkul = BAHASA PEMOGRAMAN

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

## kesimpulan

Program ini menentukan bilangan terbesar dari serangkaian input pengguna menggunakan perulangan dan kondisi. Pengguna dapat terus memasukkan bilangan hingga mengetik 0hingga berhenti. Program ini mengajarkan dasar-dasar pemrograman seperti penggunaan variabel, perulangan, kondisi, dan kontrol alur.


