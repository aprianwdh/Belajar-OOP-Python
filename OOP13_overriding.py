class Karakter:
    def __init__(self,nama,gender):
        self.__nama = nama
        self.__gender = gender

    def showInfo(self):
        return f"nama : {self.__nama} || gender : {self.__gender}"
    

class Rusher(Karakter):
    def __init__(self, nama, gender,skillDamage):
        super().__init__(nama, gender)
        self.__skillDamage = skillDamage

    #override methode
    def showInfo(self):
        infoSuper =  super().showInfo()
        return f"{infoSuper} || skill : {self.__skillDamage}"
    

class Support(Karakter):
    def __init__(self, nama, gender,skillSupport):
        super().__init__(nama, gender)
        self.__skillSupuort = skillSupport

    #override method
    def showInfo(self):
        infoSuper =  super().showInfo()
        return f"{infoSuper} || skill : {self.__skillSupuort}"
    
alok = Rusher("Alok","Pria","Dj ring")
Rafaela = Support("Rafaela","Wanita","Until I Died")

print(alok.showInfo())
print(Rafaela.showInfo())