class Bookinglist:
    def __init__(self , bookinglist_name, bookinglist_nim, bookinglist_hp, bookinglist_umur):
        self.bookinglist_name = bookinglist_name
        self.bookinglist_nim = bookinglist_nim
        self.bookinglist_hp = bookinglist_hp
        self.bookinglist_umur = bookinglist_umur
        
class JadwalKonsuler:
    def __init__(self,jadwalKonsuler_hari,jadwalKonsuler_nama,jadwalKonsuler_status,jadwalKonsuler_waktu):
        self.jadwalKonsuler_hari = jadwalKonsuler_hari
        self.jadwalKonsuler_nama = jadwalKonsuler_nama
        self.jadwalKonsuler_status = jadwalKonsuler_status
        self.jadwalKonsuler_waktu = jadwalKonsuler_waktu



def display_bookinglist(self):
    print(f"Name: {self.bookinglist_name}")
    print(f"NIM: {self.bookinglist_nim}")
    print(f"Phone: {self.bookinglist_hp}")
    print(f"Age: {self.bookinglist_umur}")