# def fact(n):
#     if n==1 or n==0:
#         return 1
#     return n*fact(n-1)

# print(fact(1))







# a = [1,2,[4,1,[1,[1,[1,[4]]]]]]

# extends
# a = isinstance(a, str)
# print(a)

# b = []
# if isinstance(a,int):
#  b.extend(a)
#  print(b)


# Sum of natural number

# def sum(n):
    
#     if n>0:
#         return n + sum(n-1)
#     return 0

# a = sum(10)
# print(f"Sum is {a}")
    
    
# def demo():
#     print("hello")
#     demo()  #recursion


# demo() # this is calling function


# def demo():
#     print("hello")
#     demo()
    
# demo()

# Write a python program for printing n to 1 sequence

# n= int(input("Enter value of n: "))
n = int(input("Enter value of n:"))
def natural(n):
    
    if n==0:
        return 
    print(n)
    return natural(n-1)
    

natural(n)



