class Bookinglist:
    def __init__(self , bookinglist_name, bookinglist_nim, bookinglist_hp):
        self.bookinglist_name = bookinglist_name
        self.bookinglist_nim = bookinglist_nim
        self.bookinglist_hp = bookinglist_hp

class JadwalKonsuler:
    def __init__(self,jadwalKonsuler_hari,jadwalKonsuler_nama,jadwalKonsuler_status):
        self.jadwalKonsuler_hari = jadwalKonsuler_hari
        self.jadwalKonsuler_nama = jadwalKonsuler_nama
        self.jadwalKonsuler_status = jadwalKonsuler_status

jadwal = [
    JadwalKonsuler('senin','Sena',True),
    JadwalKonsuler('selasa','Selia',True),
    JadwalKonsuler('rabu','Rabita',True),
    JadwalKonsuler('kamis','Kamila',True),
    JadwalKonsuler('jumat','Jumarni',True)
]

ascii_art = """
  __        __   _                            _ 
  \ \      / /__| | ___ ___  _ __ ___   ___  | |
   \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | |
    \ V  V /  __/ | (_| (_) | | | | | |  __/ |_|
     \_/\_/ \___|_|\___\___/|_| |_| |_|\___| (_)
"""

print(ascii_art)
data_list = [0,0,0,0,0]
menu = True
while menu==True:
    print("Selamat datang di aplikasi konseling")
    print("1. Registrasi")
    print("2. Tampilkan Jadwal")
    print("3. Keluar aplikasi")
    pilihan_menu = int(input("Silahkan memilih menu anda: "))

    if pilihan_menu == 1:   
        hariKonseling = input('Masukkan hari Konseling : ') 

        if hariKonseling.lower()=='senin':
            if jadwal[0].jadwalKonsuler_status == True :
                print("Masukan biodata anda:")
                nama = input("Nama : ")
                nim = input("NIM : ")
                hp = input("No HP : ")
                id= 1
                jadwal[0].jadwalKonsuler_status = False
                print('Jadwal telah di tambahkan \n')
            else :
                print('Jadwal sudah penuh \n')
        elif hariKonseling.lower()=='selasa':
             if jadwal[1].jadwalKonsuler_status == True :
                print("Masukan biodata anda:")
                nama = input("Nama : ")
                nim = input("NIM : ")
                hp = input("No HP : ")
                id= 2
                jadwal[1].jadwalKonsuler_status = False
                print('Jadwal telah di tambahkan \n')
             else :
                print('Jadwal sudah penuh \n')
            
        elif hariKonseling.lower()=='rabu':
            if jadwal[2].jadwalKonsuler_status == True :
                print("Masukan biodata anda:")
                nama = input("Nama : ")
                nim = input("NIM : ")
                hp = input("No HP : ")
                id= 3
                jadwal[2].jadwalKonsuler_status = False
                print('Jadwal telah di tambahkan \n')
            else :
                print('Jadwal sudah penuh \n')
        elif hariKonseling.lower()=='kamis':
            if jadwal[3].jadwalKonsuler_status == True :
                print("Masukan biodata anda:")
                nama = input("Nama : ")
                nim = input("NIM : ")
                hp = input("No HP : ")
                id= 4
                jadwal[3].jadwalKonsuler_status = False
                print('Jadwal telah di tambahkan \n')
            else :
                print('Jadwal sudah penuh \n')
        elif hariKonseling.lower()=='jumat':
            if jadwal[4].jadwalKonsuler_status == True :
                print("Masukan biodata anda:")
                nama = input("Nama : ")
                nim = input("NIM : ")
                hp = input("No HP : ")
                id= 5
                jadwal[4].jadwalKonsuler_status = False
                print('Jadwal telah di tambahkan \n')
            else :
                print('Jadwal sudah penuh \n')
        
        else:
            print('Input tidak valid')
            
        
        if 'nama' in locals() and 'nim' in locals() and 'hp' in locals():
            data_konseling = Bookinglist(nama, nim, hp)
            del data_list[id - 1]
            data_list.insert(id - 1, data_konseling)
        else:
            print('Biodata tidak lengkap. Registrasi dibatalkan.\n')


    elif pilihan_menu == 2:
        n= 0
        for list in jadwal:
            if list.jadwalKonsuler_status== True:
                tersedia = 'Available'
                print ('=====================================')
                print('Hari : ',list.jadwalKonsuler_hari)
                print("Konsuler : ",list.jadwalKonsuler_nama)
                print("Status : ",tersedia)
                print ('=====================================')
                n += 1
            
            else:
                tidakTersedia = 'Not Available'
                print ('=====================================')
                print('Hari : ',list.jadwalKonsuler_hari)
                print("Konsuler : ",list.jadwalKonsuler_nama)
                print("Status : ",tidakTersedia)
                print('di Booking oleh : ',data_list[n].bookinglist_name)
                print('NIM : ',data_list[n].bookinglist_nim)
                print('No hp : ',data_list[n].bookinglist_hp)
                print ('=====================================')
                n += 1

        jawaban = input("Apakah ada yang ingin di hapus ? (y/t)")
        if jawaban.lower() == 'y' :
            tujuanHapus = (input('Hari apa yang ingin di hapus ? '))
            if tujuanHapus.lower() == 'senin' :
                if jadwal[0].jadwalKonsuler_status == False :
                    jadwal[0].jadwalKonsuler_status = True
                    print('Jadwal telah di hapus \n')
            if tujuanHapus.lower() == 'selasa' :
                if jadwal[1].jadwalKonsuler_status == False :
                    jadwal[1].jadwalKonsuler_status = True
                    print('Jadwal telah di hapus \n')
            if tujuanHapus.lower() == 'rabu' :
                if jadwal[2].jadwalKonsuler_status == False :
                    jadwal[2].jadwalKonsuler_status = True
                    print('Jadwal telah di hapus \n')
            if tujuanHapus.lower() == 'kamis' :
                if jadwal[3].jadwalKonsuler_status == False :
                    jadwal[3].jadwalKonsuler_status = True
                    print('Jadwal telah di hapus \n')
            if tujuanHapus.lower() == 'jumat' :
                if jadwal[4].jadwalKonsuler_status == False :
                    jadwal[4].jadwalKonsuler_status = True
                    print('Jadwal telah di hapus \n')
            else : 
                print('Input tidak valid')
            
    elif pilihan_menu == 3:
        print("Terima kasih telah menggunakan aplikasi ini")
        break
    
    else:
            print("Input tidak valid")
