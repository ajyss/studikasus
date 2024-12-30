# TUGAS BAHASA PEMROGRAMAN
# Data Diri

Nama : Muhammad Aziz Tri Ramadhan

NIM : 312410380

Kelas : TI,24.A.3

# Output code

![](/image.png)


# Output jika tidak sesuai perintah


![](/image%20copy%202.png)

![](/image%20copy.png)



1. Struktur Program:
- Program menggunakan class bernama `ValidasiPendaftaran` yang berfungsi sebagai wadah untuk semua fungsi validasi dan data
- Memiliki dictionary `self.data` untuk menyimpan data pendaftaran (nama, telepon, email)

2. Fungsi Validasi Nama (`validasi_nama`):
```python
def validasi_nama(self, nama):
    nama = nama.strip()  # Menghapus spasi di awal dan akhir
    if not nama:  # Cek apakah kosong
        return False, "Error: Nama tidak boleh kosong"
    if len(nama) < 2:  # Cek panjang minimum
        return False, "Error: Nama terlalu pendek (minimal 2 karakter)"
    if not all(c.isalpha() or c.isspace() for c in nama):  # Cek karakter
        return False, "Error: Nama hanya boleh berisi huruf dan spasi"
    return True, nama
```
- Fungsi ini memastikan nama hanya berisi huruf
- Mengecek panjang minimal nama (2 karakter)
- Menghapus spasi di awal dan akhir nama

3. Fungsi Validasi Telepon (`validasi_telepon`):
```python
def validasi_telepon(self, telepon):
    telepon = telepon.replace(" ", "").replace("-", "")  # Bersihkan format
    if not telepon:
        return False, "Error: Nomor telepon tidak boleh kosong"
    if not telepon.isdigit():
        return False, "Error: Nomor telepon hanya boleh berisi angka"
    if len(telepon) < 8 or len(telepon) > 15:
        return False, "Error: Panjang nomor telepon harus 8-15 digit"
    return True, telepon
```
- Menghapus spasi dan tanda hubung dari nomor telepon
- Memastikan hanya berisi angka
- Mengecek panjang nomor (8-15 digit)

4. Fungsi Validasi Email (`validasi_email`):
```python
def validasi_email(self, email):
    email = email.strip()
    if not email:
        return False, "Error: Email tidak boleh kosong"
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        return False, "Error: Format email tidak valid (contoh: nama@domain.com)"
    return True, email
```
- Menggunakan regex (regular expression) untuk validasi format email
- Memastikan email memiliki format yang benar (contoh@domain.com)

5. Fungsi Input Data (`input_data`):
```python
def input_data(self):
    print("\n=== FORM PENDAFTARAN ONLINE ===")
    while True:
        nama = input("\nNama lengkap: ")
        valid, result = self.validasi_nama(nama)
        if valid:
            self.data['nama'] = result
            break
        print(result)
    # ... (proses serupa untuk telepon dan email)
```
- Menampilkan form pendaftaran
- Menggunakan loop while untuk memastikan input valid
- Menyimpan data yang valid ke dalam dictionary

6. Fungsi Tampilkan Hasil (`tampilkan_hasil`):
```python
def tampilkan_hasil(self):
    print("\n=== HASIL VALIDASI PENDAFTARAN ===")
    print("Data pendaftaran valid!")
    print(f"Nama      : {self.data['nama']}")
    print(f"Telepon   : {self.data['telepon']}")
    print(f"Email     : {self.data['email']}")
```
- Menampilkan data yang telah divalidasi dalam format yang rapi

7. Fungsi Main:
```python
def main():
    try:
        pendaftaran = ValidasiPendaftaran()
        pendaftaran.input_data()
        pendaftaran.tampilkan_hasil()
    except KeyboardInterrupt:
        print("\n\nProgram dihentikan oleh user.")
    except Exception as e:
        print(f"\nTerjadi kesalahan: {str(e)}")
    finally:
        print("\nProgram selesai.")
```
- Fungsi utama yang menjalankan program
- Memiliki penanganan error (try-except) untuk:
  - KeyboardInterrupt (jika user menekan Ctrl+C)
  - Exception umum lainnya

Cara kerja program:
1. User diminta memasukkan nama, telepon, dan email
2. Setiap input divalidasi sesuai kriteria
3. Jika input tidak valid, user diminta memasukkan ulang
4. Setelah semua data valid, hasil ditampilkan

Apakah ada bagian tertentu yang ingin Anda pahami lebih detail?