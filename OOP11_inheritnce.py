class Hero:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    @property
    def getName(self):
        pass

    @property
    def getHealth(self):
        pass

    @getName.getter
    def getName(self):
        return self.__name
    
    @getHealth.getter
    def getHealth(self):
        return self.__health
    
class Fighter(Hero):
    pass

Khalid = Hero("Khalid",100)
print(Khalid.getName)
print(Khalid.getHealth)
print(Khalid.__dict__)
print("\n")
Alpha = Fighter("Alpha",999)
print(Alpha.getName)
print(Alpha.getHealth)
print(Alpha.__dict__)

