#untuk tampilin Jadwal
def tampilkan_Jadwal() : 
    print('Senin : ',daftarJadwal['Senin']['Name'],', ',daftarJadwal['Senin']['Time'])
    print('Selasa : ',daftarJadwal['Selasa']['Name'],', ',daftarJadwal['Selasa']['Time'])
    print('Rabu : ',daftarJadwal['Rabu']['Name'],', ',daftarJadwal['Rabu']['Time'])
    print('Kamis : ',daftarJadwal['Kamis']['Name'],', ',daftarJadwal['Kamis']['Time'])
    print('Jumat : ',daftarJadwal['Jumat']['Name'],', ',daftarJadwal['Jumat']['Time'])

daftarJadwal = {
    'Senin' : {
        'Name' : 'Sena',
        'Time' : '08:00 - 15:00',
        'Status' : 'Available'
    },
    'Selasa' : {
        'Name' : 'Selia',
        'Time' : '08:00 - 15:00',
        'Status' : 'Available'
    },
    'Rabu' : {
        'Name' : 'Rabita',
        'Time' : '08:00 - 15:00',
        'Status' : 'Available'
    },
    'Kamis' : {
        'Name' : 'Kamila',
        'Time' : '08:00 - 15:00',
        'Status' : 'Available'
    },
    'Jumat' : {
        'Name' : 'Jumarni',
        'Time' : '08:00 - 12:00',
        'Status' : 'Available'
    },
}

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

