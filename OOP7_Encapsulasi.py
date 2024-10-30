class Hero:

    def __init__(self,name,health):
        self.__name = name
        self.__health = health

    #getter
    def getName(self):
        return self.__name
    
    def getHealth(self):
        return self.__health
    
    #setter
    def diserang(self,enemyPower):
        self.__health -= enemyPower

Diroths = Hero("Diroths",9999)
print(Diroths.getName())
print(Diroths.getHealth())
Diroths.diserang(9998)
print(Diroths.getHealth())
