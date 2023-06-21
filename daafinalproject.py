import os
def clear_console():
    # Clear console for different operating systems
    os.system('cls' if os.name == 'nt' else 'clear')

#untuk tampilin Jadwal
def tampilkan_Jadwal() : 
    clear_console()
    print("----------------------------------------------------------------")
    print('Senin   : {: <15}{: <8}'.format(daftarJadwal['Senin']['Name'], daftarJadwal['Senin']['Time']),' ID : ' ,daftarJadwal['Senin']['id'])
    print('Selasa  : {: <15}{: <8}'.format(daftarJadwal['Selasa']['Name'], daftarJadwal['Selasa']['Time']),' ID : ' ,daftarJadwal['Selasa']['id'])
    print('Rabu    : {: <15}{: <8}'.format(daftarJadwal['Rabu']['Name'], daftarJadwal['Rabu']['Time']),' ID : ' ,daftarJadwal['Rabu']['id'])
    print('Kamis   : {: <15}{: <8}'.format(daftarJadwal['Kamis']['Name'], daftarJadwal['Kamis']['Time']),' ID : ' ,daftarJadwal['Kamis']['id'])
    print('Jumat   : {: <15}{: <8}'.format(daftarJadwal['Jumat']['Name'], daftarJadwal['Jumat']['Time']),' ID : ' ,daftarJadwal['Jumat']['id'])
    print("----------------------------------------------------------------")

daftarJadwal = {
    'Senin' : {
        'id' : 1,
        'Name' : 'Sena',
        'Time' : '08:00 - 15:00',
        'Status' : 'Available'
    },
    'Selasa' : {
        'id' : 2,
        'Name' : 'Selia',
        'Time' : '08:00 - 15:00',
        'Status' : 'Available'
    },
    'Rabu' : {
        'id' : 3,
        'Name' : 'Rabita',
        'Time' : '08:00 - 15:00',
        'Status' : 'Available'
    },
    'Kamis' : {
        'id' : 4,
        'Name' : 'Kamila',
        'Time' : '08:00 - 15:00',
        'Status' : 'Available'
    },
    'Jumat' : {
        'id' : 5,
        'Name' : 'Jumarni',
        'Time' : '08:00 - 12:00',
        'Status' : 'Available'
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


def jadwalStatus():
    print("----------------------------------------------------------------")
    print('Senin : ',daftarJadwal['Senin']['Name'], daftarJadwal['Senin']['Status'])
    print('Selasa : ',daftarJadwal['Selasa']['Name'], daftarJadwal['Selasa']['Status'])
    print('Rabu : ',daftarJadwal['Rabu']['Name'], daftarJadwal['Rabu']['Status'])
    print('Kamis : ',daftarJadwal['Kamis']['Name'], daftarJadwal['Kamis']['Status'])
    print('Jumat : ',daftarJadwal['Jumat']['Name'], daftarJadwal['Jumat']['Status'])
    print("----------------------------------------------------------------")

def menu():
     while True:
        print("Selamat datang di aplikasi konseling")
        print("1. Masukan biodata")
        print("2. Jadwal yang sudah di booking")
        print("3. Keluar aplikasi")
        pilihan_menu = int(input("Silahkan memilih menu anda: "))

        if pilihan_menu == 1:
            # menu 1
            print("Masukan biodata anda:")
            nama = input("Nama : ")
            nim = input("NIM : ")
            usia = input("Usia : ")
            kasus = input("Deskripsi Masalah : ")
            hariKonseling = input('Masukkan hari Konseling : ')
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
                  
            # Kembali ke menu utama
            input("Tekan Enter untuk kembali ke menu utama.")

        elif pilihan_menu == 2:
            # menu 2
            print("Berikut jadwal yang sudah di booking")
            jadwalStatus()
        elif pilihan_menu == 3:
            # keluar aplikasi
            print("Terima kasih telah menggunakan aplikasi ini")
            break  
        else:
            print("Input tidak valid")


ascii_art = """
  __        __   _                            _ 
  \ \      / /__| | ___ ___  _ __ ___   ___  | |
   \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | |
    \ V  V /  __/ | (_| (_) | | | | | |  __/ |_|
     \_/\_/ \___|_|\___\___/|_| |_| |_|\___| (_)
"""

print(ascii_art)

Username = input("Masukan username anda: ")
print("Selamat datang,"+Username)
tampilkan_Jadwal()
menu()
