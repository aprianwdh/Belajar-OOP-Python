class Hero:
    def __init__(self,name,health,atckPower,defense):
        
        self.name = name
        self.health = health
        self.atckPower = atckPower
        self.defense = defense

    def menyerang(self,target):
        print (f"{self.name} menyerang {target.name} dengana damage {self.atckPower}")
        target.diserang(self.name,self.atckPower)

    def diserang(self,penyerang,damage_amount):
        print(f"\n{self.name} diserang oleh {penyerang}")
        damage_diterima = max( damage_amount - self.defense,0)
        print(F"Damage yang diterima = {damage_diterima} ")
        self.health -= damage_diterima
        print(f"sisa health = {self.health}")
    

balmon = Hero("Balmon",100,10,10)
natan = Hero("Natan",80,15,9)

while True:
    balmon.menyerang(natan)
    print("\n")
    natan.menyerang(balmon)

    if natan.health <= 0 or balmon.health <= 0:
        break