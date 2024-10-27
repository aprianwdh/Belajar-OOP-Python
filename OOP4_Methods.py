class Hero:
    #variabel class
    jumlah_hero = 0

    def __init__(self,inputNama,inputPower,inputDefense,inputHealth):
        self.name = inputNama
        self.Power = inputPower
        self.Defense = inputDefense
        self.health = inputHealth
        Hero.jumlah_hero += 1

    #void method / void tanpa argument dan method
    def sayhi(self):
        print(f"Halo nama saya {self.name}")

    #method dengan argument
    def Spell(self,inspire):
        self.Power += inspire

    #method dengan argument dan return
    def take_damage(self,damage_amount):
        self.health -= damage_amount
        return f'hp dari {self.name} = {self.health}'


hero1 = Hero("Angela",50,90,100)

#memanggil method void
hero1.sayhi()

#memanggil method
hero1.Spell(90)
print(hero1.Power)

#memanggil method
print(hero1.take_damage(10))

