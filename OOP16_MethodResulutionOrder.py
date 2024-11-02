class A:
    def show(self):
        return "Ini class A"
    
class B:
    def show(self):
        return "Ini class B"
    
class Alp(A,B):
    #urutannya alp,A,B
    def show(self):
        return "Ini class alph"
    pass

alph = Alp()
# print(alph.show())

class Role:
    def __init__(self,role):
        self.role = role

    def show_role(self):
        return self.role
    
class Gender:
    def __init__(self,gender):
        self.gender = gender

    def show_gender(self):
        return self.gender

class Karakter(Role,Gender):
    def __init__(self, nama, role, gender):
        self.nama = nama
        super().__init__(role)
        Gender.__init__(self,gender)

adit = Karakter("adit","Plenker","Lakiks")

adit_dict = adit.__dict__

for key,value in adit_dict.items():
    print(f"{key} : {value}")
