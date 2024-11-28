class Mobil:
    def __init__(self,nama,kelamin):
        self.nama = nama
        self.kelamin = kelamin

class MObilIndo(Mobil):
    def __init__(self,nama, kelamin,terbang):
        super().__init__(nama, kelamin)
        self.terbang = terbang

Avanza = MObilIndo('kak','asa',True)

print(Avanza.__dict__)