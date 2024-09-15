# class Test():
#     a =5
#     b = 100
#     print(a)
    
# obj1 =Test()
# print(obj1)


# obj1.a = 10
# print(obj1.a)


class Test2():
    name = "Broadway"
    subject = "python"
    
    def teaching(aaaaa):
        return "I am studying python at Broadway"
    
obj1 = Test2()
print(obj1.teaching())

class Test2():
    name = "Broadway"
    subject = "Python"
    
    def teaching(aa):
        return f"I am studying {aa.subject} at {aa.name}"
    
obj1 = Test2()
print(obj1.teaching())






class Test2():
    name = "Broadway"
    subject = "java"

   

    def teaching(self):
        return f'i am teaching {self.subject} at {self.name}'
    
    def __str__(self) -> str:
        return "this is test class"

# obj1 = Test2()
# print(obj1)
# print(obj1.teaching())

class Test3():

    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def test(self):
        return self.a
    

obj2 = Test3("hello","world")
print(obj2.test())

class Math():
    def __init__(self,num1,num2) -> None:
        self.a = num1
        self.b = num2


    def add(self):
        return self.a + self.b
    
    def diff(self):
        return self.a - self.b
    
    def mul(self):
        return self.a * self.b
    
obj=Math(6,7)
print(obj.add())
print(obj.diff())


        
