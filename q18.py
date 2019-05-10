class Building:
    def __init__(self,name):
        self.name = name
    def named(self):
        return f"nameis {self.name}"
class Appartment(Building):
    def __init__(self,name):
        super().__init__(name)#1 way
class House(Building):
    def __init__(self):
        super().__init__('shrestha')# 2 way
class Commercial(Building):
    def __init__(self):
        super().__init__('khadka')

c1 = Building('mannat')
c2 = Appartment('giri')
c3 = House()
c4 = Commercial()
print(c1.named())
print(c2.named())
print(c3.named())
print(c4.named())


