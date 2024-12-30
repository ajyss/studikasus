import re

class ValidasiPendaftaran:
    def __init__(self):
        self.data = {
            'nama': '',
            'telepon': '',
            'email': ''
        }

    def validasi_nama(self, nama):
        """Validasi format nama"""
        # Menghapus spasi di awal dan akhir
        nama = nama.strip()
        
        # Cek apakah nama kosong
        if not nama:
            return False, "Error: Nama tidak boleh kosong"
        
        # Cek panjang minimum nama
        if len(nama) < 2:
            return False, "Error: Nama terlalu pendek (minimal 2 karakter)"
            
        # Cek apakah hanya berisi huruf dan spasi
        if not all(c.isalpha() or c.isspace() for c in nama):
            return False, "Error: Nama hanya boleh berisi huruf dan spasi"
            
        return True, nama

    def validasi_telepon(self, telepon):
        """Validasi format nomor telepon"""
        # Menghapus semua spasi dan tanda hubung
        telepon = telepon.replace(" ", "").replace("-", "")
        
        # Cek apakah nomor telepon kosong
        if not telepon:
            return False, "Error: Nomor telepon tidak boleh kosong"
            
        # Cek apakah hanya berisi angka
        if not telepon.isdigit():
            return False, "Error: Nomor telepon hanya boleh berisi angka"
            
        # Cek panjang nomor telepon
        if len(telepon) < 8 or len(telepon) > 15:
            return False, "Error: Panjang nomor telepon harus 8-15 digit"
            
        return True, telepon

    def validasi_email(self, email):
        """Validasi format email"""
        # Menghapus spasi di awal dan akhir
        email = email.strip()
        
        # Cek apakah email kosong
        if not email:
            return False, "Error: Email tidak boleh kosong"
            
        # Pattern untuk validasi email
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        # Cek format email
        if not re.match(pattern, email):
            return False, "Error: Format email tidak valid (contoh: nama@domain.com)"
            
        return True, email

    def input_data(self):
        """Meminta input data dari user"""
        print("\n=== FORM PENDAFTARAN ONLINE ===")
        print("Silakan masukkan data Anda:")
        
        while True:
            nama = input("\nNama lengkap: ")
            valid, result = self.validasi_nama(nama)
            if valid:
                self.data['nama'] = result
                break
            print(result)

        while True:
            telepon = input("Nomor telepon: ")
            valid, result = self.validasi_telepon(telepon)
            if valid:
                self.data['telepon'] = result
                break
            print(result)

        while True:
            email = input("Email: ")
            valid, result = self.validasi_email(email)
            if valid:
                self.data['email'] = result
                break
            print(result)

    def tampilkan_hasil(self):
        """Menampilkan hasil pendaftaran"""
        print("\n=== HASIL VALIDASI PENDAFTARAN ===")
        print("Data pendaftaran valid!")
        print(f"Nama      : {self.data['nama']}")
        print(f"Telepon   : {self.data['telepon']}")
        print(f"Email     : {self.data['email']}")
        print("================================")

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

if __name__ == "__main__":
    main()