import os
import colorama

colorama.init()

BLUE = colorama.Fore.BLUE
RED = colorama.Fore.RED
GREEN = colorama.Fore.GREEN
RESET = colorama.Style.RESET_ALL

biodata = {}

def clear_console():
    # Clear console for different operating systems
    os.system('cls' if os.name == 'nt' else 'clear')

def menu(biodata):
    while True:
        clear_console()
        tampilkan_Jadwal()
        print("Selamat datang di aplikasi konseling")
        print("1. Masukkan biodata")
        print("2. Jadwal yang sudah di booking")
        print("3. Keluar aplikasi")
        pilihan_menu = int(input("Silahkan memilih menu Anda: "))

        if pilihan_menu == 1:
            # Menu 1 - Masukkan biodata
            
            print("Masukkan biodata anda:")
            nama = input("Nama: ")
            nim = input("NIM: ")
            usia = input("Usia: ")
            kasus = input("Deskripsi Masalah: ")
            hariKonseling = input('Masukkan hari Konseling: ')
            if hariKonseling == 'Senin' :
                  cekSenin()
            elif hariKonseling == 'Selasa' :
                  cekSelasa()
            elif hariKonseling == 'Rabu' :
                  cekRabu()
            elif hariKonseling == 'Kamis' :
                  cekKamis()
            elif hariKonseling == 'Jumat' :
                  cekJumat()
            else :
                print("Hari konseling tidak valid")
            
            biodata = {}
            biodata[nim] = {'nama': nama, 'usia': usia, 'kasus': kasus}

            print("Biodata telah berhasil dimasukkan.")
            
    

            # Kembali ke menu utama
            input("Tekan Enter untuk kembali ke menu utama.")

        elif pilihan_menu == 2:
            # Menu 2 - Jadwal yang sudah di booking
            jadwalStatus(biodata)

            # Kembali ke menu utama
            input("Tekan Enter untuk kembali ke menu utama.")

        elif pilihan_menu == 3:
            # Keluar aplikasi
            print("Terima kasih telah menggunakan aplikasi ini.")
            break

        else:
            print("Input tidak valid")

def tampilkan_Jadwal():
    clear_console()
    print("----------------------------------------------------------------")
    print('Senin   : {: <15}{: <8}'.format(daftarJadwal['Senin']['Name'], \
        daftarJadwal['Senin']['Time']), ' ID : ', daftarJadwal['Senin']['id'])
    print('Selasa  : {: <15}{: <8}'.format(daftarJadwal['Selasa']['Name'], \
        daftarJadwal['Selasa']['Time']), ' ID : ', daftarJadwal['Selasa']['id'])
    print('Rabu    : {: <15}{: <8}'.format(daftarJadwal['Rabu']['Name'], \
        daftarJadwal['Rabu']['Time']), ' ID : ', daftarJadwal['Rabu']['id'])
    print('Kamis   : {: <15}{: <8}'.format(daftarJadwal['Kamis']['Name'], \
        daftarJadwal['Kamis']['Time']), ' ID : ', daftarJadwal['Kamis']['id'])
    print('Jumat   : {: <15}{: <8}'.format(daftarJadwal['Jumat']['Name'], \
        daftarJadwal['Jumat']['Time']), ' ID : ', daftarJadwal['Jumat']['id'])
    print("----------------------------------------------------------------")

daftarJadwal = {
    'Senin': {
        'id': 1,
        'Name': 'Sena',
        'Time': '08:00 - 15:00',
        'Status': 'Available'
    },
    'Selasa': {
        'id': 2,
        'Name': 'Selia',
        'Time': '08:00 - 15:00',
        'Status': 'Available'
    },
    'Rabu': {
        'id': 3,
        'Name': 'Rabita',
        'Time': '08:00 - 15:00',
        'Status': 'Available'
    },
    'Kamis': {
        'id': 4,
        'Name': 'Kamila',
        'Time': '08:00 - 15:00',
        'Status': 'Available'
    },
    'Jumat': {
        'id': 5,
        'Name': 'Jumarni',
        'Time': '08:00 - 12:00',
        'Status': 'Available'
    },
}

def cekSenin() :
    if daftarJadwal['Senin']['Status']== 'Available' :
        print('Jadwal booking anda telah di tambahkan')
        daftarJadwal['Senin']['Status'] = 'Not Available'
    else :
        print('Jadwal booking sudah penuh')
                    
def cekSelasa() :
    if daftarJadwal['Selasa']['Status'] == 'Available' :
        print('Jadwal booking anda telah di tambahkan')
        daftarJadwal['Selasa']['Status'] = 'Not Available'
    else :
        print('Jadwal booking sudah penuh')

def cekRabu() :       
    if daftarJadwal['Rabu']['Status'] == 'Available' :
        print('Jadwal booking anda telah di tambahkan')
        daftarJadwal['Rabu']['Status'] = 'Not Available'
    else :
        print('Jadwal booking sudah penuh')

def cekKamis() :      
    if daftarJadwal['Kamis']['Status'] == 'Available' :
        print('Jadwal booking anda telah di tambahkan')
        daftarJadwal['Kamis']['Status'] = 'Not Available'
    else :
        print('Jadwal booking sudah penuh')

def cekJumat() :     
    if daftarJadwal['Jumat']['Status'] == 'Available' :
        print('Jadwal booking anda telah di tambahkan')
        daftarJadwal['Jumat']['Status'] = 'Not Available'
    else :
        print('Jadwal booking sudah penuh')


def jadwalStatus(biodata):
    
    print("----------------------------------------------------------------")
    if daftarJadwal['Senin']['Status'] == 'Not Available' :
        print('Senin  :', daftarJadwal['Senin']['Name'], daftarJadwal['Senin']['Status'], \
            biodata)
    elif daftarJadwal['Selasa']['Status'] == 'Not Available' :
        print('Selasa  :', daftarJadwal['Selasa']['Name'], daftarJadwal['Selasa']['Status'], \
            biodata)
    elif daftarJadwal['Rabu']['Status'] == 'Not Available' :
        print('Rabu  :', daftarJadwal['Rabu']['Name'], daftarJadwal['Rabu']['Status'], \
            biodata)
    elif daftarJadwal['Kamis']['Status'] == 'Not Available' :
        print('Kamis  :', daftarJadwal['Kamis']['Name'], daftarJadwal['Kamis']['Status'], \
            biodata)
    elif daftarJadwal['Jumat']['Status'] == 'Not Available' :
        print('Jumat  :', daftarJadwal['Jumat']['Name'], daftarJadwal['Jumat']['Status'], \
            biodata)
    print("----------------------------------------------------------------")


ascii_art = """
  __        __   _                            _ 
  \ \      / /__| | ___ ___  _ __ ___   ___  | |
   \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | |
    \ V  V /  __/ | (_| (_) | | | | | |  __/ |_|
     \_/\_/ \___|_|\___\___/|_| |_| |_|\___| (_)
"""

print(ascii_art)

Username = input("Masukkan username anda: ")
print("Selamat datang, " + Username)
tampilkan_Jadwal()
menu(biodata)
