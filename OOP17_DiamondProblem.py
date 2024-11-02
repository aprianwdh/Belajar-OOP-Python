class A:
    def show(self):
        return "Ini Show A"
    
class B(A):
    def show(self):
        return "Ini Show B"
    
class C(A):
    def show(self):
        return "Ini Show C"
    
class D(B,C):
    pass

objek = D()

#jadi urutannya d,b,c,a
help(objek)