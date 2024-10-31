import random

class Hero:
    #class var
    __jumlah = 0

    def __init__(self,name,health,attpower,armor):
        self.__name = name
        self.__BaseHealth = health
        self.__BeseAttPower = attpower
        self.__BaseArmor = armor
        self.__level = 1
        self.__exp = 0

        self.MaxHealth = self.__BaseHealth * self.__level
        self.Attpower = self.__BeseAttPower * self.__level
        self.Armor = self.__BaseArmor * self.__level

        Hero.__jumlah += 1

    @property
    def show_info(self):
        print(f"""
Name = {self.__name}
Health = {self.__BaseHealth}/{self.MaxHealth}
AttPower = {self.Attpower}
Armor = {self.Armor}
Level = {self.__level}
Exp = {self.__exp}
""")
        
    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self,addExp):
        print(f"exp diperoleh = {addExp}")
        self.__exp += addExp

        if self.__exp >= 100:
            print(f"{self.__name} Level Up!!!!!!!")
            self.__level += 1

            self.MaxHealth = self.__BaseHealth * self.__level
            self.Attpower = self.__BeseAttPower * self.__level
            self.Armor = self.__BaseArmor * self.__level

            self.__exp -= 100
    
    def menyerang(self,target):
        exprndm = random.randint(1,100)
        print (f"{self.__name} menyerang {target.__name}")
        self.gainExp = exprndm
        

        

Alucrot = Hero("Alucrot",100,50,10)
saber = Hero("Saber",90,55,10)

Alucrot.menyerang(saber)
Alucrot.show_info