nama = input("Silahkan masukkan nama user: ")
print("Halo, " + nama)
menu = ""  # Inisialisasi variabel menu

data_mahasiswa = {}

while menu != "5":
    print("Selamat Datang di Aplikasi Pengelolaan IPK")
    print("================================================================")
    print("1. Input Data Mahasiswa")
    print("2. Lihat / Edit Data Mahasiswa")
    print("3. Urutkan Nama Mahasiswa Berdasarkan Nama / NIM")
    print("4. Pencarian Data Mahasiswa Berdasarkan Nama / NIM")
    print("5. Keluar Aplikasi")
    print("================================================================")
    menu = input("Silahkan Pilih Menu Anda: ")
    print("================================================================")
    if menu == "1":
        print("Anda memilih Menu 1: Input Data Mahasiswa")
        # Tambahkan kode untuk memproses input data mahasiswa di sini
        print("================================================================")
        jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))

        for i in range(jumlah_mahasiswa):
            print(f"Masukkan data untuk mahasiswa ke-{i+1}:")
            mahasiswa = input("Masukan nama mahasiswa: ")
            nim = input("Masukan NIM mahasiswa: ")
            fakultas = input("Masukan fakultas mahasiswa: ")
            jurusan = input("Masukan jurusan mahasiswa: ")
            print("================================================================")
            matkul = int(input("Masukan jumlah mata kuliah: "))
            print("================================================================")
            mata_kuliah = {}
            for j in range(matkul):
                nama_matkul = input(f"Masukan nama mata kuliah ke-{j+1}: ")
                sks_matkul = int(input(f"Masukan jumlah sks mata kuliah {nama_matkul}: "))
                nilai_matkul = int(input(f"Masukan nilai {nama_matkul}: "))
                print("================================================================")
                mata_kuliah[nama_matkul] = {
                    'mata kuliah': nama_matkul,
                    'jumlah SKS': sks_matkul,
                    'nilai': nilai_matkul,
                }

            data_mahasiswa[nim] = {
                'nama': mahasiswa,
                'fakultas': fakultas,
                'jurusan': jurusan,
                'mata_kuliah': mata_kuliah,
                'nim': nim,
            }
        print("Data mahasiswa telah dimasukkan")
        print("================================================================")
    elif menu == "2":
        print("Anda memilih Menu 2: Lihat / Edit Data Mahasiswa")
        print("================================================================")
    # Tambahkan kode untuk melihat atau mengedit data mahasiswa di sini
        print("Data Mahasiswa:")
        for nim, mhs in data_mahasiswa.items():
            print("================================================================")
            print("NIM: ", nim)
            print("Nama: ", mhs['nama'])
            print("Fakultas: ", mhs['fakultas'])
            print("Jurusan: ", mhs['jurusan'])
            print("Mata Kuliah dan Nilai: ")
            
            for mata_kuliah, detail in mhs['mata_kuliah'].items():
                print("  - Mata Kuliah: ", mata_kuliah)
                print("    Jumlah SKS: ", detail['jumlah SKS'])
                print("    Nilai: ", detail['nilai'])
                if int(detail['nilai']) >= 95:
                    detail['grade'] = "A+"
                elif int(detail['nilai']) >= 90:
                    detail['grade'] = "A"
                elif int(detail['nilai']) >= 85:
                    detail['grade'] = "B+"
                elif int(detail['nilai']) >= 80:
                    detail['grade'] = "B"
                elif int(detail['nilai']) >= 75:
                    detail['grade'] = "C+"
                elif int(detail['nilai']) >= 70:
                    detail['grade'] = "C"
                elif int(detail['nilai']) >= 65:
                    detail['grade'] = "D"
                else:
                    detail['grade'] = "E"

            print("Grade:", detail['grade'])

            total_sks = 0
            total_bobot = 0

            for nama_matkul, detail_matkul in mhs['mata_kuliah'].items():
                sks_matkul = int(detail_matkul['jumlah SKS'])
                nilai_matkul = int(detail_matkul['nilai'])

                total_sks += sks_matkul
                total_bobot += sks_matkul * nilai_matkul

            if total_sks > 0:
                ipk = total_bobot / total_sks
                if ipk > 4:
                    ipk = 4
                    print("IPK Mahasiswa:", ipk)
            else:
                print("Belum ada mata kuliah yang diinput")
        
        else:
            print("Data mahasiswa dengan NIM tersebut tidak ditemukan")
            pilihan = input("Apakah Anda ingin mengedit data mahasiswa ini? (y/n): ")

            if pilihan == "y":
            # Tambahkan kode untuk mengedit data mahasiswa sesuai kebutuhan Anda
                    nama_baru = input("Masukkan nama baru: ")
                    data_mahasiswa[nim]['nama'] = nama_baru
                    fakultas_baru = input("Masukkan fakultas baru: ")
                    data_mahasiswa[nim]['fakultas'] = fakultas_baru
                    jurusan_baru = input("Masukkan jurusan baru: ")
                    data_mahasiswa[nim]['jurusan'] = jurusan_baru
                    nilai_baru = input("Masukkan nilai baru: ")
                    mata_kuliah[nama_matkul]['nilai'] = nilai_baru
                    sks_baru = input("Masukkan nilai baru: ")
                    mata_kuliah[nama_matkul]['jumlah SKS'] = sks_baru

                    print("Data mahasiswa berhasil diubah.")
            else:
                    print("Data mahasiswa tidak diubah.")

    elif menu == "3":
        print("Anda memilih Menu 3: Urutkan Nama Mahasiswa Berdasarkan Nama / NIM")
        print("================================================================")
        # Tambahkan kode untuk mengurutkan data mahasiswa berdasarkan nama atau NIM di sini
        pilihan_urutan = input("Pilih urutan (1. Nama / 2. NIM): ")
        print("================================================================")
        if pilihan_urutan == "1":
        # Mengurutkan berdasarkan nama
            mahasiswa_sorted = sorted(data_mahasiswa.values(), key=lambda x: x['nama'])
        elif pilihan_urutan == "2":
        # Mengurutkan berdasarkan NIM
            mahasiswa_sorted = sorted(data_mahasiswa.values(), key=lambda x: x['nim'])
        else:
            print("Pilihan urutan tidak valid.")

    # Menampilkan data mahasiswa yang sudah diurutkan
        print("Data Mahasiswa (Setelah Diurutkan): ")
        print("================================================================")
        for mhs in mahasiswa_sorted:
            print("Nama: ", mhs['nama'])
            print("Fakultas: ", mhs['fakultas'])
            print("Jurusan: ", mhs['jurusan'])
            print("NIM: ", mhs['nim'])
            print("Mata Kuliah dan Nilai: ")
        for mata_kuliah, detail in mhs['mata_kuliah'].items():
            print("  - Mata Kuliah: ", mata_kuliah)
            print("    Jumlah SKS: ", detail['jumlah SKS'])
            print("    Nilai: ", detail['nilai'])
        print("================================================================")
    elif menu == "4":
        print("Anda memilih Menu 4: Pencarian Data Mahasiswa Berdasarkan Nama / NIM")
        print("================================================================")
        # Tambahkan kode untuk mencari data mahasiswa berdasarkan nama atau NIM di sini
        nim = input("Masukkan NIM mahasiswa yang ingin Anda lihat: ")
        print("================================================================")

        if nim in data_mahasiswa:
            print("Data mahasiswa:")
            print("Nama:", data_mahasiswa[nim]['nama'])
            print("Fakultas:", data_mahasiswa[nim]['fakultas'])
            print("Jurusan:", data_mahasiswa[nim]['jurusan'])
            print("Mata Kuliah: ")

            for nama_matkul, detail_matkul in data_mahasiswa[nim]['mata_kuliah'].items():
                print("  - Nama Mata Kuliah:", nama_matkul)
                print("    Jumlah SKS:", detail_matkul['jumlah SKS'])
                print("    Nilai:", detail_matkul['nilai'])
                print("Grade:", detail_matkul['grade'])
                print("IPK Mahasiswa:", ipk)
        print("================================================================")
                
    elif menu == "5":
        print("Terima kasih telah mengunakan aplikasi ini...")
        print("================================================================")
        # Tambahkan kode untuk keluar dari aplikasi di sini
        break
    else:
        print("Menu yang Anda pilih tidak valid.")
        print("================================================================")
