import os

class Bookinglist:
    def __init__(self, bookinglist_name, bookinglist_nim, bookinglist_usia):
        self.bookinglist_name = bookinglist_name
        self.bookinglist_nim = bookinglist_nim
        self.bookinglist_usia = bookinglist_usia

class JadwalKonsuler:
    def __init__(self, jadwalKonsuler_hari, jadwalKonsuler_nama, jadwalKonsuler_status):
        self.jadwalKonsuler_hari = jadwalKonsuler_hari
        self.jadwalKonsuler_nama = jadwalKonsuler_nama
        self.jadwalKonsuler_status = jadwalKonsuler_status

biodata = [None] * 5

daftarJadwal = {
    'Senin': JadwalKonsuler('Senin', 'Sena', True),
    'Selasa': JadwalKonsuler('Selasa', 'Selia', True),
    'Rabu': JadwalKonsuler('Rabu', 'Rabita', True),
    'Kamis': JadwalKonsuler('Kamis', 'Kamila', True),
    'Jumat': JadwalKonsuler('Jumat', 'Jumarni', True)
}

login_data = {
    'admin': 'admin123'
}

def clear_console():
    # Clear console for different operating systems
    os.system('cls' if os.name == 'nt' else 'clear')

def login():
    while True:
        clear_console()
        print("Silahkan login")
        username = input("Username: ")
        password = input("Password: ")

        if username in login_data.keys() and login_data[username] == password:
            print("Login berhasil!")
            input("Tekan Enter untuk melanjutkan...")
            menu()
            break
        else:
            print("Username atau password salah!")
            input("Tekan Enter untuk mencoba lagi...")

def pemasukan_biodata():
    print("Masukkan biodata anda:")
    nama = input("Nama: ")
    nim = input("NIM: ")
    usia = input("Usia: ")
    kasus = input("Deskripsi Masalah: ")
    
    print("Jadwal yang tersedia:")
    penampilan_jadwal_status()
    
    harikonseling = input("Masukan Hari Konseling: ").capitalize()

    if harikonseling in daftarJadwal.keys():
        if daftarJadwal[harikonseling].jadwalKonsuler_status:
            daftarJadwal[harikonseling].jadwalKonsuler_status = False
            index = list(daftarJadwal.keys()).index(harikonseling)
            biodata[index] = Bookinglist(nama, nim, usia)
            print('Jadwal telah ditambahkan \n')
        else:
            print("Hari Konseling tidak tersedia.")
    else:
        print("Hari Konseling tidak valid.")

    print(biodata)

def penampilan_jadwal_status():
    for jadwal in daftarJadwal.values():
        if jadwal.jadwalKonsuler_status:
            tersedia = 'Available'
            print('=====================================')
            print('Hari :', jadwal.jadwalKonsuler_hari)
            print("Konsuler :", jadwal.jadwalKonsuler_nama)
            print("Status :", tersedia)
            print('=====================================')
        else:
            tidakTersedia = 'Not Available'
            n = list(daftarJadwal.values()).index(jadwal)
            print ('=====================================')
            print('Hari :', jadwal.jadwalKonsuler_hari)
            print("Konsuler :", jadwal.jadwalKonsuler_nama)
            print("Status :", tidakTersedia)
            print("Nama : ", biodata[n].bookinglist_name)
            print('NIM :', biodata[n].bookinglist_nim)
            print('Usia :', biodata[n].bookinglist_usia)
            print('=====================================')

def edit_biodata():
    penampilan_jadwal_status()
    print("Edit biodata booking:")
    jawab = input("Apakah anda ingin mengedit data yang dimasukkan? (y/t) \n")
    if jawab.lower() == 'y':
        jawab_hari = input("Masukkan hari yang ingin diedit: ").capitalize()
        if jawab_hari in daftarJadwal.keys():
            n = list(daftarJadwal.keys()).index(jawab_hari)
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
                if not daftarJadwal[jawab_hari].jadwalKonsuler_status:
                    daftarJadwal[jawab_hari].jadwalKonsuler_status = True
                    print('Jadwal telah dihapus \n')
        else:
            print("Hari yang dimasukkan tidak valid.")
    else:
        print("Anda tidak mengedit")

def menu():
    while True:
        clear_console()
        print("Selamat datang di aplikasi konseling")
        print("1. Masukkan biodata")
        print("2. Jadwal yang sudah di booking")
        print("3. Edit biodata")
        print("4. Keluar aplikasi")
        pilihan_menu = input("Silahkan pilih menu Anda: ")

        if pilihan_menu == '1':
            # Menu 1 - Masukkan biodata
            pemasukan_biodata()
            input("Tekan Enter untuk kembali ke menu utama...")
        elif pilihan_menu == '2':
            # Menu 2 - Jadwal yang sudah di booking
            print("Jadwal yang sudah di booking:")
            penampilan_jadwal_status()
            input("Tekan Enter untuk kembali ke menu utama...")
        elif pilihan_menu == '3':
            # Menu 3 - Edit biodata
            edit_biodata()
            input("Tekan Enter untuk kembali ke menu utama...")
        elif pilihan_menu == '4':
            # Menu 4 - Keluar aplikasi
            print("Terima kasih telah menggunakan aplikasi ini.")
            break

login()
