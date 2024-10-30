class Hero:

    #class variabel
    jumlah_hero = 0

    def __init__(self,name,health):
        self.name = name
        self.health = health

        #private variabel
        self.__private = "ini private ajah"

        #protacted variabel
        self._protected = "ini protected ygy"
        

miya = Hero("Miya",100)
print(miya.__dict__)
miya._protected = "sioki"
print(miya.__dict__)