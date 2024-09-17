# Use any of function and carry out exception/error handling

# Arithmetic Error
def division(a,b):
    try:
        divide = a/b
        print(f"Result: {divide}")
        
    except ArithmeticError:
        print("Error: Arithmetic error occured!")
        

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

division(a,b)


# Index Error
def list(data, index):
    try:
        result = data[index]
        print(f"Result: {result}")
    except IndexError:
        print("Error is Index out of range")
        

a = [1,2,3,4,5,6]
index = int(input('Enter index: '))
list(a,index)