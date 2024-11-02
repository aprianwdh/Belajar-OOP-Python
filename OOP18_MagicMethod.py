#magic method ditandai dengan double underscore (__method__)
class Durian:

    #Magic method __init__
    def __init__(self,nama,jumlah):
        self.nama = nama
        self.jumlah = jumlah

    #unutk mengganti ouput objeck bila diprint 
    def __repr__(self):
        return f"Object dengan nama {self.nama} telah dibuat"
    
    def __str__(self):
        return f"Object dengan nama {self.nama} telah dibuat"
    
    #Untuk menambahkan value dua objek
    def __add__(self,other):
        return self.jumlah + other.jumlah
    
    #untuk mengganti output __dict__
    @property
    def __dict__(self):
        return f"nama = {self.nama}\njumlah = {self.jumlah}"

Durian1 = Durian("Durian Afrika",10)
Durian2 = Durian("Durian Jepang",100)

print(Durian1 + Durian2)
print(Durian1.__dict__)