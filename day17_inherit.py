class Parent():
    a = 10
    b = 11

class Child(Parent):
    c = 50
    # a = 777

obj = Child()
print(obj.a)

'''

- make a 2 class parent and child 
- parent class should have 2 method as well as child
- child class object should access parent class method

'''



# class Parent():
#     def __init__(self) -> None:
#         self.d = 12

#     def method1(self):
#         return "parent method 1"

#     def method2(self):
#         return "Parent method 2"

# class Child(Parent):
#     def __init__(self):
#         self.a = 22
#         super().__init__(self)
        

#     def method3(self):
#         return "child method 3"

#     def method4(self):
#         return "child method 4"
    
# obj = Child()
# print(obj.method1())
# print(obj.a)
# print(obj.d)





