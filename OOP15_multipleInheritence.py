class Role:
    def __init__(self, role):
        self.role = role

    def show_role(self):
        return f"Role : {self.role}"
    
class Fraksi:
    def __init__(self, fraksi):
        self.fraksi = fraksi

    def show_fraksi(self):
        return f"Fraksi : {self.fraksi}"
    

class Hero(Role, Fraksi):
    def __init__(self, nama, role, fraksi):
        self.nama = nama
        super().__init__(role)  # Menggunakan super() untuk memanggil __init__ dari Role
        Fraksi.__init__(self,fraksi)

    def show_hero(self):
        return f"Nama : {self.nama}, {self.show_role()}, {self.show_fraksi()}"
        

# Contoh penggunaan
Alpha = Hero("Alpha", "fighter", "Moniyan")

print(Alpha.show_hero())    # Output: Nama : Alpha, Role : fighter, Fraksi : Moniyan
print(Alpha.show_fraksi())  
print(Alpha.show_role())  
