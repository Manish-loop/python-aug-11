# Polymorphism - same name with different work

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print(self.brand, self.model)
        
    def move(self):
        print("Move")
        
class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")
        
class Plane(Vehicle):
    def move(self):
        print("Fly!")
        
car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")










