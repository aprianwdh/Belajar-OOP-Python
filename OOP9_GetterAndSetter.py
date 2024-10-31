class Hero:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    @property
    def info(self):
        return "***INFO***\nname {}\nhealth {}".format(self.__name,self.__health)
    
    @property
    def health(self):
        pass

    @health.getter
    def health(self):
        return self.__health
    
    @health.setter
    def health(self,input):
        self.__health = input

    @health.deleter
    def health(self):
        print("Armor di delet")
        self.__health = None

Tigreal = Hero("Tigreal",100)

# print(Tigreal.info)

print(Tigreal.__dict__)
print(Tigreal.health)
Tigreal.health = 99999
print(Tigreal.health)
print(Tigreal.__dict__)
del Tigreal.health
print(Tigreal.__dict__)
