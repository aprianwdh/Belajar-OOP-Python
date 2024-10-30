class Hero:
    __jumlah_Hero = 0

    def __init__(self,nama):
        self.__name = nama
        Hero.__jumlah_Hero += 1

    #hanya berlaku untuk objek karena ada self
    def getJumlah1(self):
        return self.__jumlah_Hero
    
    #hanya berlaku unutk class
    def getJumlah2():
        return Hero.__jumlah_Hero
    
    #ststic method bisa unutk keduanya
    @staticmethod
    def getjumlah3():
        return Hero.__jumlah_Hero
    
    #classmethod 
    @classmethod
    def getjumlah4(cls):
        return cls.__jumlah_Hero
    
miya = Hero("MIya")
# hanya berlakau unutk object
print(miya.getJumlah1())
Kon = Hero("Kon")
print(miya.getJumlah1())

# hanya berlakau unutk Class
print(Hero.getJumlah2())

#bisa unutk keduanya
print(miya.getjumlah3())
print(Hero.getjumlah3())

print(miya.getjumlah4())
print(Hero.getjumlah4())


