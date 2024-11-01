class Mobil:
    def __init__(self,merk,warna,kecepatan,jenis):
        
        self.__merk = merk
        self.__warna = warna
        self.__kecepatan = kecepatan
        self.__jenis = jenis

    def show_info(self):
        print(f"merk \t\t= {self.__merk}")
        print(f"warna \t\t= {self.__warna}")
        print(f"kecepatan \t= {self.__kecepatan}")
        print(f"jenis \t\t= {self.__jenis}")


    @property
    def getMerk(self):
        pass
    @getMerk.getter
    def getMerk(self):
        return self.__merk
    @getMerk.setter
    def getMerk(self,addinput):
        self.__merk = addinput

    @property
    def getWarna(self):
        pass
    @getWarna.getter
    def getWarna(self):
        return self.__warna
    @getWarna.setter
    def getWarna(self,addinput):
        self.__warna = addinput
    
    @property
    def getKecepatan(self):
        pass
    @getKecepatan.getter
    def getKecepatan(self):
        return self.__kecepatan
    @getKecepatan.setter
    def getKecepatan(self,addinput):
        self.__kecepatan = addinput
    
    @property
    def getJenis(self):
        pass
    @getJenis.getter
    def getJenis(self):
        return self.__jenis
    @getJenis.setter
    def getJenis(self,addinput):
        self.__jenis = addinput
    
class MobilKeluarga(Mobil):
    def __init__(self, merk, warna, kecepatan, jenis = "Mobil Keluarga",kapasitas = 7):
        super().__init__(merk, warna, kecepatan, jenis)
        self.__kapasitas = kapasitas

    def show_info(self):
        super().show_info()
        print(f"kapasitas \t={self.__kapasitas}")


Avanza = MobilKeluarga("Avanza","Hitam",100)

Avanza.getKecepatan = 9999
# Avanza.show_info()
dictd = Avanza.__dict__
# print(dictd)

for key,value in dictd.items():
    print(f"{key} : {value}")






