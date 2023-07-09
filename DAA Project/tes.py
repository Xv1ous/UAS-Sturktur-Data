from Jadwal import Bookinglist
from Jadwal import JadwalKonsuler

jadwal = {
    'senin_a': JadwalKonsuler('senin', 'Sena', True, '08:00 - 12:00'),
    'senin_b': JadwalKonsuler('senin', 'Adiarja', True, '12:00 - 16:00'),
    'selasa_a': JadwalKonsuler('selasa', 'Selia', True, '08:00 - 12:00'),
    'selasa_b': JadwalKonsuler('selasa', 'Elizabeth', True, '12:00 - 16:00'),
    'rabu_a': JadwalKonsuler('rabu', 'Rabita', True, '08:00 - 12:00'),
    'rabu_b': JadwalKonsuler('rabu', 'Leon', True, '12:00 - 16:00'),
    'kamis_a': JadwalKonsuler('kamis', 'Kamila', True, '08:00 - 12:00'),
    'kamis_b': JadwalKonsuler('kamis', 'Tiffa', True, '12:00 - 16:00'),
    'jumat_a': JadwalKonsuler('jumat', 'Jumarni', True, '08:00 - 12:00'),
    'jumat_b': JadwalKonsuler('jumat', 'Kafka', True, '12:00 - 16:00')
}

nama_file = 'data_booking.txt'  # Nama file untuk menyimpan data

# Fungsi untuk menyimpan data ke dalam file
def simpan_data_ke_file(data, nama_file):
    with open(nama_file, 'w') as file:
        for key, value in data.items():
            if key in jadwal:  # Memastikan hanya menyimpan data yang ada di jadwal
                file.write(f"{key},{value}\n")

# Fungsi untuk membaca data dari file
def baca_data_dari_file(nama_file):
    data = {}
    with open(nama_file, 'r') as file:
        for line in file:
            key, value = line.strip().split(',')
            data[key] = value
    return data

# Mengambil data booking dari file (jika ada)
try:
    data_booking = baca_data_dari_file(nama_file)
except FileNotFoundError:
    data_booking = {}

# Masukkan biodata jika jadwal tersedia
hari_konseling = input('Masukkan hari yang akan dipilih:').lower()
jam_konseling = input('Masukkan jam yang ingin dipilih (08:00 - 12:00(A) dan 12:00 - 16:00(B)): ').lower()
key = f"{hari_konseling}_{jam_konseling}"
if key in jadwal and jadwal[key].jadwalKonsuler_status:
    print("Masukkan biodata anda:")
    nama = input("Nama : ")
    nim = input("NIM : ")
    hp = input("No HP : ")
    umur = input("Umur : ")

    jadwal[key].jadwalKonsuler_status = False
    print('Jadwal telah ditambahkan \n')

    data_booking[key] = nama
else:
    print('Jadwal sudah penuh \n')

# Simpan data booking ke file
simpan_data_ke_file(data_booking, nama_file)

# Cetak jadwal dan data booking
for key, value in jadwal.items():
    print('=====================================')
    print('Hari : ', value.jadwalKonsuler_hari)
    print('Konsuler : ', value.jadwalKonsuler_nama)
    print('Waktu : ', value.jadwalKonsuler_waktu)

    if key in data_booking:
        print('Status : Not Available')
        print('di Booking oleh : ', data_booking[key])
    else:
        print('Status : Available')
    
    print('=====================================')
