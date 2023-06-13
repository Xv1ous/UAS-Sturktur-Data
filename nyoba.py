# Inisialisasi list barang
daftar_jadwal = []

# Fungsi untuk menambahkan barang
def tambah_jadwal(nama_barang, waktu_konsul):
    barang = {
        'nama': nama_barang,
        'waktu': waktu_konsul,
    }
    daftar_jadwal.append(barang)
# Menambahkan barang ikan, minyak, dan telur ke dalam daftar
tambah_jadwal("agus", "senin 10:00")
tambah_jadwal("bambang", "Senin 11:00")
tambah_jadwal("rojak", "selasa 12:00")

# Menampilkan daftar barang
print("Daftar Jadwal:")
for barang in daftar_jadwal:
    print(f"- {barang['nama']}, Waktu: {barang['waktu']}")

# Fungsi untuk menghapus barang
def hapus_barang(nama_barang):
    for barang in daftar_jadwal:
        if barang['nama'] == nama_barang:
            daftar_jadwal.remove(barang)
            print(f"Barang '{nama_barang}' telah dihapus.")
            return
    print(f"Barang '{nama_barang}' tidak ditemukan.")

# Fungsi untuk menampilkan daftar barang
def tampilkan_daftar_barang():
    print("Daftar Jadwal:")
    if len(daftar_jadwal) == 0:
        print("Tidak ada barang yang tersedia.")
    else:
        for barang in daftar_jadwal:
            print(f"- {barang['nama']}, Waktu: {barang['waktu']}")

# Fungsi untuk menjual barang
def jual_barang(nama_barang):
    for barang in daftar_jadwal:
        if barang['nama'] == nama_barang:
            daftar_jadwal.remove(barang)
            print(f"Barang '{nama_barang}' terjual.")
            return
    print(f"Barang '{nama_barang}' tidak ditemukan.")

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print(f"- {barang['nama']}, Waktu: {barang['waktu']}")
    print("=== Menu ===")
    print("1. Booking Jadwal")
    print("2. Hapus Jadwa;")
    print("3. Tampilkan Daftar Jadwal")
    print("5. Keluar")
    print()

# Loop utama
while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == '1':
        nama = input("Masukkan nama siswa: ")
        waktu = input("Masukkan Waktu Konseling: ")
        tambah_jadwal(nama, waktu)
    elif pilihan == '2':
        nama = input("Masukkan nama barang yang ingin dihapus: ")
        hapus_barang(nama)
    elif pilihan == '3':
        tampilkan_daftar_barang()
    elif pilihan == '4':
        nama = input("Masukkan nama barang yang terjual: ")
        jual_barang(nama)
    elif pilihan == '5':
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih angka menu yang tersedia.")
