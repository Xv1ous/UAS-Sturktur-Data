import os

class Bookinglist:
    def __init__(self, bookinglist_name, bookinglist_nim, bookinglist_usia, \
        bookinglist_kasus):
        self.bookinglist_name = bookinglist_name
        self.bookinglist_nim = bookinglist_nim
        self.bookinglist_usia = bookinglist_usia
        self.bookinglist_kasus = bookinglist_kasus

class JadwalKonsuler:
    def __init__(self, jadwalKonsuler_hari, jadwalKonsuler_nama, \
        jadwalKonsuler_status,jadwalKonsuler_time):
        self.jadwalKonsuler_hari = jadwalKonsuler_hari
        self.jadwalKonsuler_nama = jadwalKonsuler_nama
        self.jadwalKonsuler_status = jadwalKonsuler_status
        self.jadwalKonsuler_time = jadwalKonsuler_time

biodata = [None] * 10

daftarJadwal = {
    'Senin':[ JadwalKonsuler('Senin', 'Sena', True, '08:00 - 12:00'),
             JadwalKonsuler('Senin', 'Adiarja', True, '12:00 - 16:00'),
            ],
    'Selasa':[JadwalKonsuler('Selasa', 'Selia', True, '08:00 - 12:00'),
              JadwalKonsuler('Selasa', 'Elizabeth', True, '12:00 - 16:00')
              ],
    'Rabu':[JadwalKonsuler('Rabu', 'Rabita', True, '08:00 - 12:00'),
            JadwalKonsuler('Rabu', 'Leon', True, '12:00 - 16:00'),
    ],
    'Kamis':[ JadwalKonsuler('Kamis', 'Kamila', True, '08:00 - 12:00',),
             JadwalKonsuler('Rabu', 'Tiffa', True, '12:00 - 16:00'),
    ],
    'Jumat':[ JadwalKonsuler('Jumat', 'Jumarni', True, '08:00 - 12:00',),
             JadwalKonsuler('Rabu', 'Kafka', True, '12:00 - 16:00'),
    ],
}

def clear_console():
    # Clear console for different operating systems
    os.system('cls' if os.name == 'nt' else 'clear')

login_admin = {
    'admin': 'admin123'
}

def login():
    while True:
        clear_console()
        print("Silahkan login")
        username = input("Username: ")
        password = input("Password: ")

        if username in login_admin.keys() and login_admin[username] == password:
            print("Login berhasil!")
            input("Tekan Enter untuk melanjutkan...")
            menu()
            break
        else:
            print("Username atau password salah!")
            input("Tekan Enter untuk mencoba lagi...")

def pemasukan_biodata():
    n = 0
    if daftarJadwal[list(daftarJadwal.keys())[n]][0].jadwalKonsuler_status:
        print("Masukkan biodata anda:")
        nama = input("Nama: ")
        nim = input("NIM: ")
        usia = input("Usia: ")
        kasus = input("Deskripsi Masalah: ")
        harikonseling = input("Masukan Hari Konseling: ").lower()
        jamkonseling = input("Masukan jam yang ingin pilih (08:00 - 12:00(A) dan 12:00 - 16:00(B)): ")
          
        if harikonseling == 'senin':
            if jamkonseling.lower() == 'a':
                daftarJadwal[list(daftarJadwal.keys())[0]][0].jadwalKonsuler_status = False
                biodata[0] = Bookinglist(nama, nim, usia, kasus)
                print('Jadwal telah ditambahkan \n')
            elif jamkonseling.lower() == 'b':
                daftarJadwal[list(daftarJadwal.keys())[0]][1].jadwalKonsuler_status = False
                biodata[1] = Bookinglist(nama, nim, usia, kasus)
                print('Jadwal telah ditambahkan \n')
            
        elif harikonseling == 'selasa':
            if jamkonseling.lower() == 'a':
                daftarJadwal[list(daftarJadwal.keys())[1]][0].jadwalKonsuler_status = False
                biodata[2] = Bookinglist(nama, nim, usia, kasus)
                print('Jadwal telah ditambahkan \n')
            elif jamkonseling.lower() == 'b':
                daftarJadwal[list(daftarJadwal.keys())[1]][1].jadwalKonsuler_status = False
                biodata[3] = Bookinglist(nama, nim, usia, kasus)
                print('Jadwal telah ditambahkan \n')
            
        elif harikonseling == 'rabu':
            if jamkonseling.lower() == 'a':
                daftarJadwal[list(daftarJadwal.keys())[2]][0].jadwalKonsuler_status = False
                biodata[4] = Bookinglist(nama, nim, usia, kasus)
                print('Jadwal telah ditambahkan \n')
            elif jamkonseling.lower() == 'b':
                daftarJadwal[list(daftarJadwal.keys())[2]][1].jadwalKonsuler_status = False
                biodata[5] = Bookinglist(nama, nim, usia, kasus)
                print('Jadwal telah ditambahkan \n')
            
        elif harikonseling == 'kamis':
            if jamkonseling.lower() == 'a':
                daftarJadwal[list(daftarJadwal.keys())[3]][0].jadwalKonsuler_status = False
                biodata[6] = Bookinglist(nama, nim, usia, kasus)
                print('Jadwal telah ditambahkan \n')
            elif jamkonseling.lower() == 'b':
                daftarJadwal[list(daftarJadwal.keys())[3]][1].jadwalKonsuler_status = False
                biodata[7] = Bookinglist(nama, nim, usia, kasus)
                print('Jadwal telah ditambahkan \n')
            
        elif harikonseling == 'jumat':
            if jamkonseling.lower() == 'a':
                daftarJadwal[list(daftarJadwal.keys())[4]][0].jadwalKonsuler_status = False
                biodata[8] = Bookinglist(nama, nim, usia, kasus)
                print('Jadwal telah ditambahkan \n')
            elif jamkonseling.lower() == 'b':
                daftarJadwal[list(daftarJadwal.keys())[4]][1].jadwalKonsuler_status = False
                biodata[9] = Bookinglist(nama, nim, usia, kasus)
                print('Jadwal telah ditambahkan \n')
        else:
            print("Hari konseling tidak valid.")

        
        print(biodata)
        
def penampilan_jadwal_status():
    n = 0
    
    for jadwal in daftarJadwal.values():
        if jadwal[n].jadwalKonsuler_status:
                tersedia = 'Available'
                print('=====================================')
                print('Hari :', jadwal[n].jadwalKonsuler_hari)
                print('Konsuler :', jadwal[n].jadwalKonsuler_nama)
                print('Status :', tersedia)
                print('=====================================')
        else:
            tidakTersedia = 'Not Available'
            for j in jadwal:
                n = list(daftarJadwal.values()).index(jadwal)
                print('=====================================')
                print('Hari :', j.jadwalKonsuler_hari)
                print('Jam :', j.jadwalKonsuler_time)
                print('Konsuler :', j.jadwalKonsuler_nama)
                print('Status :', tidakTersedia)
                print('Dibooking oleh :', biodata[n].bookinglist_name)
                print('NIM :', biodata[n].bookinglist_nim)
                print('Usia :', biodata[n].bookinglist_usia)
                print('=====================================')
                    


def edit_biodata():
    penampilan_jadwal_status()
    print("Edit biodata booking:")
    jawab = input("Apakah anda ingin mengedit data yang di masukan (y/t) \n")
    if jawab.lower == 'y':
        jawab_hari = input("Entry hari apa yang ingin diedit? :\n").lower()
        if jawab_hari in map(str.lower, daftarJadwal.keys()):
            n = list(map(str.lower, daftarJadwal.keys())).index(jawab_hari)
            jawaban_nama = input("Apakah anda ingin mengedit nama? (y/t)\n")
            if jawaban_nama.lower() == 'y':
                new_name = input("Masukkan nama: ")
                biodata[n].bookinglist_name = new_name
            jawaban_nim = input("Apakah anda ingin mengedit NIM? (y/t)\n")
            if jawaban_nim.lower() == 'y':
                new_nim = input("Masukkan NIM: ")
                biodata[n].bookinglist_nim = new_nim
            jawaban_usia = input("Apakah anda ingin mengedit usia? (y/t)\n")
            if jawaban_usia.lower() == 'y':
                new_usia = input("Masukkan usia: ")
                biodata[n].bookinglist_usia = new_usia
            jawaban_harikonseling = input("Apakah anda ingin menghapus jadwal untuk hari ini? (y/t)\n")
            if jawaban_harikonseling.lower() == 'y':
                if not daftarJadwal[list(daftarJadwal.keys())[n]][0].jadwalKonsuler_status:
                    daftarJadwal[list(daftarJadwal.keys())[n]][0].jadwalKonsuler_status = True
                    print('Jadwal telah dihapus \n')
        else:
            print("Hari yang dimasukkan tidak valid.")
    else:
        print("Anda tidak mengedit")

def menu():
    while True:
        print("Selamat datang di aplikasi konseling")
        print("1. Masukkan biodata")
        print("2. Jadwal yang sudah di booking")
        print("3. Edit Biodata")
        print("4. Keluar aplikasi")
        pilihan_menu = input("Silahkan memilih menu Anda: ")

        if pilihan_menu == '1':
            # Menu 1 - Masukkan biodata
            pemasukan_biodata()
            input("Tekan Enter untuk kembali ke menu utama...")
            
        elif pilihan_menu == '2':
            # Menu 2 - Jadwal yang sudah di booking
            print("Jadwal yang sudah di booking:")
            penampilan_jadwal_status()
            # Kembali ke menu utama
            input("Tekan Enter untuk kembali ke menu utama...")
            clear_console()
        elif pilihan_menu == '3':
            # Menu 3 - Edit biodata
            edit_biodata()
            input("Tekan Enter untuk kembali ke menu utama...")
            clear_console()
        elif pilihan_menu == '4':
            # Menu 4 - Keluar aplikasi
            print("Terimakasih telah mengunakan aplikasi ini.")
            break
        else:
            print("Menu tidak valid. Silakan pilih menu yang tersedia!")

menu()
