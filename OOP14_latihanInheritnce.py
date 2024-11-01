class Karakter:
    def __init__(self,name):
        self.health_pool = [0,0,0,0,0]
        self.armor_pool = [0,0,0,0,0]
        self.power_pool = [0,0,0,0,0]
        self.__name = name
        self.__exp = 0
        self.__level = 0

        self.__health = 0
        self.__armor = 0
        self.__power = 0

    def show_info(self):
        return f"nama : {self.__name} || health : {self.__health} || armor : {self.__armor} || power : {self.__power} || level : {self.__level}"
        
    @property
    def level_up(self):
        pass

    @property
    def gain_exp(self):
        pass

    @gain_exp.setter
    def gain_exp(self,addinput):
        self.__exp += addinput

        while self.__exp >= 100:
            self.level_up = 1
            self.__exp -= 100

    @level_up.setter
    def level_up(self,addinput):
        self.__level += addinput
        self.__health = self.health_pool[self.__level]
        self.__armor = self.armor_pool[self.__level]
        self.__power= self.power_pool[self.__level]


class Fighter(Karakter):
    def __init__(self, name):
        super().__init__(name)
        self.health_pool = [100,200,300,400,500]
        self.armor_pool = [2,4,6,8,10]
        self.power_pool = [10,20,30,40,50]
        self.level_up = 1

class Mage(Karakter):
    def __init__(self, name):
        super().__init__(name)
        self.health_pool = [50,100,150,200,250]
        self.armor_pool = [2,4,6,8,10]
        self.power_pool = [15,30,45,60,75]
        self.level_up = 1

Balmond = Fighter("Balmond")
print(Balmond.show_info())
Balmond.gain_exp = 200
print(Balmond.show_info())

print("\n")

Carmila = Mage("carmila")
print(Carmila.show_info())
Carmila.gain_exp = 200
print(Carmila.show_info())
