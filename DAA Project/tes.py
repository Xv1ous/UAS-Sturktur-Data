from Jadwal import Bookinglist
from Jadwal import JadwalKonsuler
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

n=0

hari_konseling = input('Masukkan hari yang akan di pilih:').lower()
jam_konseling = input('Masukan jam yang ingin pilih (08:00 - 12:00(A) dan 12:00 - 16:00(B)): ').lower()
if hari_konseling == 'senin' and jam_konseling == 'a':
    n = 0
elif hari_konseling == 'senin' and jam_konseling == 'b':
    n = 1
elif hari_konseling == 'selasa' and jam_konseling == 'a':
    n = 2
elif hari_konseling == 'selasa' and jam_konseling == 'b':
    n = 3
elif hari_konseling == 'rabu' and jam_konseling == 'a':
    n = 4
elif hari_konseling == 'rabu' and jam_konseling == 'b':
    n = 5
elif hari_konseling == 'kamis' and jam_konseling == 'a':
    n = 6
elif hari_konseling == 'kamis' and jam_konseling == 'b':
    n = 7
elif hari_konseling == 'jumat' and jam_konseling == 'a':
    n = 8
elif hari_konseling == 'jumat' and jam_konseling == 'b':
    n = 9
print("Masukan biodata anda:")
nama = input("Nama : ")
nim = input("NIM : ")
hp = input("No HP : ")
umur = input("Umur : ")

jadwal[n].jadwalKonsuler_status = False
print('Jadwal telah di tambahkan \n')

booking = Bookinglist(nama, nim, hp, umur)

for jadwal_konsuler in jadwal:
    print('================================================================')
    print(f"Hari: {jadwal_konsuler.jadwalKonsuler_hari}")
    print(f"Nama: {jadwal_konsuler.jadwalKonsuler_nama}")
    print(f"Status: {'Tersedia' if jadwal_konsuler.jadwalKonsuler_status else 'Terisi'}")
    print(f"Jam: {jadwal_konsuler.jadwalKonsuler_waktu}")
    print(f"Nama: {booking.bookinglist_name}")
    print(f"NIM: {booking.bookinglist_nim}")
    print(f"No HP: {booking.bookinglist_hp}")
    print(f"Umur: {booking.bookinglist_umur}")
    print('================================================================')