class Hero: # Template
    pass


hero1 = Hero() # object/instance
hero2 = Hero() # object/instance
hero3 = Hero() # object/instance

hero1.name = "Balmon"
hero1.health = 100

hero2.name = "Miya"
hero2.health = 90

hero3.name = "Diroth"
hero3.health = 100

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)