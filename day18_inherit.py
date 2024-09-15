# multi-level inheritance

class Parent():
    a = 10
        
       
class Child1(Parent):
    c = 12
    
    
class Child2(Child1):
    d = 100
    
    

obj = Child2()
print(obj.a)
print(obj.c)


# Multiple inheritance

class Parent():
    a = 10
    
class Child1():
    d = 12
    
class Child2(Parent, Child1):
    d = 20
    
obj = Child2()
print(obj.a, obj.d)




class Mammal():
    def mammal_info(self):
        print("Mammals can give direct birth.")
        
    def test(self):
        return 12
        
class WingedAnimal():
    def winged_animal_info(self):
        print("Winged animals can flap.")
        
    def test(self):
        return "hello"
        
        
class Bat(Mammal, WingedAnimal):
    def __init__(self):
        super.__init__(self)

# Here creating object of Bat class
b1 = Bat()

b1.mammal_info()
b1.winged_animal_info()
b1.test()
print(b1.test())


# 
