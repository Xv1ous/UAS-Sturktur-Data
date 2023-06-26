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


def clear_console():
    # Clear console for different operating systems
    os.system('cls' if os.name == 'nt' else 'clear')

def pemasukan_biodata():
    n = 0

    if daftarJadwal[list(daftarJadwal.keys())[n]].jadwalKonsuler_status:
        print("Masukkan biodata anda:")
        nama = input("Nama: ")
        nim = input("NIM: ")
        usia = input("Usia: ")
        kasus = input("Deskripsi Masalah: ")
        harikonseling = input("Masukan Hari Konseling: ").lower()  
        if harikonseling == 'senin':
            daftarJadwal[list(daftarJadwal.keys())[0]].jadwalKonsuler_status = False
            biodata[0] = Bookinglist(nama, nim, usia)
            print('Jadwal telah ditambahkan \n')
        elif harikonseling == 'selasa':
            daftarJadwal[list(daftarJadwal.keys())[1]].jadwalKonsuler_status = False
            biodata[1] = Bookinglist(nama, nim, usia)
            print('Jadwal telah ditambahkan \n')
        elif harikonseling == 'rabu':
            daftarJadwal[list(daftarJadwal.keys())[2]].jadwalKonsuler_status = False
            biodata[2] = Bookinglist(nama, nim, usia)
            print('Jadwal telah ditambahkan \n')
        elif harikonseling == 'kamis':
            daftarJadwal[list(daftarJadwal.keys())[3]].jadwalKonsuler_status = False
            biodata[3] = Bookinglist(nama, nim, usia)
            print('Jadwal telah ditambahkan \n')
        elif harikonseling == 'jumat':
            daftarJadwal[list(daftarJadwal.keys())[4]].jadwalKonsuler_status = False
            biodata[4] = Bookinglist(nama, nim, usia)
            print('Jadwal telah ditambahkan \n')
        else:
            print("Konselor Not Available")
        
        print(biodata)
        

def penampilan_jadwal_status():
    for jadwal in daftarJadwal.values():
        if jadwal.jadwalKonsuler_status:
            tersedia = 'Available'
            print('=====================================')
            print('Hari : ', jadwal.jadwalKonsuler_hari)
            print("Konsuler : ", jadwal.jadwalKonsuler_nama)
            print("Status : ", tersedia)
            print('=====================================')
        else:
            tidakTersedia = 'Not Available'
            n = list(daftarJadwal.values()).index(jadwal)
            print ('=====================================')
            print('Hari : ',jadwal.jadwalKonsuler_hari)
            print("Konsuler : ",jadwal.jadwalKonsuler_nama)
            print("Status : ",tidakTersedia)
            print('di Booking oleh : ', biodata[n].bookinglist_name)
            print('NIM : ', biodata[n].bookinglist_nim)
            print('Usia : ', biodata[n].bookinglist_usia)
            print('=====================================')

def edit_biodata():
    n = 0
    penampilan_jadwal_status()
    print("Edit biodata booking:")
    jawab = input("Apakah anda ingin mengedit data yang di masukan (y/t) \n")
    if jawab == 'y':
        jawab_hari = input("Entry hari apa yang ingin diedit ? :\n")
        if jawab_hari == 'senin':
            n=0
        elif jawab_hari == 'selasa':
            n=1
        elif jawab_hari == 'rabu':
            n=2
        elif jawab_hari == 'kamis':
            n=3
        elif jawab_hari == 'jumat':
            n=4
        else :
            print("input tidak valid")
            
        jawaban_nama = input("Apakah anda ingin mengedit nama ? (y/t)\n")
        if jawaban_nama.lower() == 'y' :
            new_name = input("Masukkan nama :")
            biodata[n].bookinglist_nama = new_name
        else:   
            print()
        jawaban_nim = input("Apakah anda ingin mengedit nim ? (y/t)\n")
        if jawaban_nim.lower() == 'y' :
            new_nim = input("Masukan NIM :")
            biodata[n].bookinglist_nim = new_nim
        jawaban_usia = input("Apakah anda ingin mengedit usia ? (y/t)\n")
        if jawaban_usia == 'y' :
            new_usia = input("Masukan usia :")
            biodata[n].bookinglist_usia = new_usia
        jawaban_harikonseling = input("Apakah anda ingin menghapus jadwal untuk hari ini ? (y/t)\n")
        if jawaban_harikonseling == 'y' :
            if daftarJadwal[n].jadwalKonsuler_status == False :
                daftarJadwal[n].jadwalKonsuler_status = True
                print('Jadwal telah di hapus \n')
            

    else:
            print("Anda tidak mengedit")

def menu():
    while True:
        print("Selamat datang di aplikasi konseling")
        print("1. Masukkan biodata")
        print("2. Jadwal yang sudah di booking")
        print("3. Keluar aplikasi")
        pilihan_menu = input("Silahkan memilih menu Anda: ")

        if pilihan_menu == '1':
            # Menu 1 - Masukkan biodata
            pemasukan_biodata()
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
        elif pilihan_menu == '4':
            # Menu 4 - Keluar aplikasi
            print("Terimakasih telah mengunakan aplikasi ini.")
            break

menu()
