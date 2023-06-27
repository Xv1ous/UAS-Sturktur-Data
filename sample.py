class Bookinglist:
    def __init__(self , bookinglist_name, bookinglist_nim, bookinglist_hp):
        self.bookinglist_name = bookinglist_name
        self.bookinglist_nim = bookinglist_nim
        self.bookinglist_hp = bookinglist_hp

class JadwalKonsuler:
    def __init__(self,jadwalKonsuler_hari,jadwalKonsuler_nama,jadwalKonsuler_status,jadwalKonsuler_waktu):
        self.jadwalKonsuler_hari = jadwalKonsuler_hari
        self.jadwalKonsuler_nama = jadwalKonsuler_nama
        self.jadwalKonsuler_status = jadwalKonsuler_status
        self.jadwalKonsuler_waktu = jadwalKonsuler_waktu

jadwal = [
    JadwalKonsuler('senin','Sena',True,'08:00 - 12:00'),
    JadwalKonsuler('senin','Adiarja',True,'12:00 - 16:00'),
    JadwalKonsuler('selasa','Selia',True,'08:00 - 12:00'),
    JadwalKonsuler('selasa','Elizabeth',True,'12:00 - 16:00'),
    JadwalKonsuler('rabu','Rabita',True,'08:00 - 12:00'),
    JadwalKonsuler('rabu','Leon',True,'12:00 - 16:00'),
    JadwalKonsuler('kamis','Kamila',True,'08:00 - 12:00'),
    JadwalKonsuler('kamis','Tiffa',True,'12:00 - 16:00'),
    JadwalKonsuler('jumat','Jumarni',True,'08:00 - 12:00'),
    JadwalKonsuler('jumat','Kafka',True,'12:00 - 16:00')
]

ascii_art = """
  __        __   _                            _ 
  \ \      / /__| | ___ ___  _ __ ___   ___  | |
   \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | |
    \ V  V /  __/ | (_| (_) | | | | | |  __/ |_|
     \_/\_/ \___|_|\___\___/|_| |_| |_|\___| (_)
"""

print(ascii_art)
data_list = [None] * 10
menu = True
while menu==True:
    print("Selamat datang di aplikasi konseling")
    print("1. Registrasi")
    print("2. Tampilkan Jadwal")
    print("3. Keluar aplikasi")
    pilihan_menu = int(input("Silahkan memilih menu anda: "))

    if pilihan_menu == 1:   
        hariKonseling = input('Masukkan hari Konseling : ') 
        jamkonseling = input("Masukan jam yang ingin pilih (08:00 - 12:00(A) dan 12:00 - 16:00(B)): ")
        if hariKonseling.lower()=='senin' and jamkonseling.lower()=='a':
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
        elif hariKonseling.lower()=='senin' and jamkonseling.lower()=='b':
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
        elif hariKonseling.lower()=='selasa' and jamkonseling.lower()=='a':
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
        elif hariKonseling.lower()=='selasa' and jamkonseling.lower()=='b':
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
        elif hariKonseling.lower()=='rabu' and jamkonseling.lower()=='a':
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
        elif hariKonseling.lower()=='rabu' and jamkonseling.lower()=='b':
             if jadwal[5].jadwalKonsuler_status == True :
                print("Masukan biodata anda:")
                nama = input("Nama : ")
                nim = input("NIM : ")
                hp = input("No HP : ")
                id= 6
                jadwal[5].jadwalKonsuler_status = False
                print('Jadwal telah di tambahkan \n')
             else :
                print('Jadwal sudah penuh \n')
        elif hariKonseling.lower()=='kamis' and jamkonseling.lower()=='a':
             if jadwal[6].jadwalKonsuler_status == True :
                print("Masukan biodata anda:")
                nama = input("Nama : ")
                nim = input("NIM : ")
                hp = input("No HP : ")
                id= 7
                jadwal[6].jadwalKonsuler_status = False
                print('Jadwal telah di tambahkan \n')
             else :
                print('Jadwal sudah penuh \n')
        elif hariKonseling.lower()=='kamis' and jamkonseling.lower()=='b':
             if jadwal[7].jadwalKonsuler_status == True :
                print("Masukan biodata anda:")
                nama = input("Nama : ")
                nim = input("NIM : ")
                hp = input("No HP : ")
                id= 8
                jadwal[7].jadwalKonsuler_status = False
                print('Jadwal telah di tambahkan \n')
             else :
                print('Jadwal sudah penuh \n')
        elif hariKonseling.lower()=='jumat' and jamkonseling.lower()=='a':
             if jadwal[8].jadwalKonsuler_status == True :
                print("Masukan biodata anda:")
                nama = input("Nama : ")
                nim = input("NIM : ")
                hp = input("No HP : ")
                id= 9
                jadwal[8].jadwalKonsuler_status = False
                print('Jadwal telah di tambahkan \n')
             else :
                print('Jadwal sudah penuh \n')
        elif hariKonseling.lower()=='jumat' and jamkonseling.lower()=='b':
             if jadwal[9].jadwalKonsuler_status == True :
                print("Masukan biodata anda:")
                nama = input("Nama : ")
                nim = input("NIM : ")
                hp = input("No HP : ")
                id= 10
                jadwal[9].jadwalKonsuler_status = False
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
                print("Waktu : ",list.jadwalKonsuler_waktu)
                print("Status : ",tersedia)
                print ('=====================================')
                n += 1
            
            else:
                tidakTersedia = 'Not Available'
                print ('=====================================')
                print('Hari : ',list.jadwalKonsuler_hari)
                print("Konsuler : ",list.jadwalKonsuler_nama)
                print("Waktu : ",list.jadwalKonsuler_waktu)
                print("Status : ",tidakTersedia)
                print('di Booking oleh : ',data_list[n].bookinglist_name)
                print('NIM : ',data_list[n].bookinglist_nim)
                print('No hp : ',data_list[n].bookinglist_hp)
                print ('=====================================')
                n += 1

        jawaban = input("Apakah ada yang ingin di hapus ? (y/t)")
        if jawaban.lower() == 'y' :
            tujuanHapus = input('Hari apa yang ingin di hapus ? ')
            tujuanWaktu = input('Masukan jam yang ingin dihapus (08:00 - 12:00(A) dan 12:00 - 16:00(B)):')
            if tujuanHapus.lower() == 'senin' and tujuanWaktu.lower()=='a':
                if jadwal[0].jadwalKonsuler_status == False :
                    jadwal[0].jadwalKonsuler_status = True
                    print('Jadwal telah di hapus \n')
            if tujuanHapus.lower() == 'senin' and tujuanWaktu.lower()=='b':
                if jadwal[1].jadwalKonsuler_status == False :
                    jadwal[1].jadwalKonsuler_status = True
                    print('Jadwal telah di hapus \n')
            if tujuanHapus.lower() == 'selasa' and tujuanWaktu.lower()=='a':
                if jadwal[2].jadwalKonsuler_status == False :
                    jadwal[2].jadwalKonsuler_status = True
                    print('Jadwal telah di hapus \n')
            if tujuanHapus.lower() == 'selasa' and tujuanWaktu.lower()=='b':
                if jadwal[3].jadwalKonsuler_status == False :
                    jadwal[3].jadwalKonsuler_status = True
                    print('Jadwal telah di hapus \n')
            if tujuanHapus.lower() == 'rabu' and tujuanWaktu.lower()=='a':
                if jadwal[4].jadwalKonsuler_status == False :
                    jadwal[4].jadwalKonsuler_status = True
                    print('Jadwal telah di hapus \n')
            if tujuanHapus.lower() == 'rabu' and tujuanWaktu.lower()=='b':
                if jadwal[5].jadwalKonsuler_status == False :
                    jadwal[5].jadwalKonsuler_status = True
                    print('Jadwal telah di hapus \n')
            if tujuanHapus.lower() == 'kamis' and tujuanWaktu.lower()=='a':
                if jadwal[6].jadwalKonsuler_status == False :
                    jadwal[6].jadwalKonsuler_status = True
                    print('Jadwal telah di hapus \n')
            if tujuanHapus.lower() == 'kamis' and tujuanWaktu.lower()=='b':
                if jadwal[7].jadwalKonsuler_status == False :
                    jadwal[7].jadwalKonsuler_status = True
                    print('Jadwal telah di hapus \n')
            if tujuanHapus.lower() == 'jumat' and tujuanWaktu.lower()=='a':
                if jadwal[8].jadwalKonsuler_status == False :
                    jadwal[8].jadwalKonsuler_status = True
                    print('Jadwal telah di hapus \n')
            if tujuanHapus.lower() == 'jumat' and tujuanWaktu.lower()=='b':
                if jadwal[9].jadwalKonsuler_status == False :
                    jadwal[9].jadwalKonsuler_status = True
                    print('Jadwal telah di hapus \n')
            
            else : 
                print('Input tidak valid')
            
    elif pilihan_menu == 3:
        print("Terima kasih telah menggunakan aplikasi ini")
        break
    
    else:
            print("Input tidak valid")
    
    else:
            print("Input tidak valid")
