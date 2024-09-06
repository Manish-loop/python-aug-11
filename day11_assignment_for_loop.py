# Multiplication table input from user, how many want to input, odd number multiplication

# n = int(input("Enter number of times:"))
# a = []
# for i in range(0 , n):
#    j = int(input(f"Enter number for {i}: "))
#    if j%2 !=0:
#     a.append(j)
    
# for data in a:    
#    for k in range(1,11):
      
#      print(f"{data} X {k} = {data*k}")


n = int(input("How many times do you want for multiplication "))
a = []

for i in range(n):
    num = int(input(f"Enter a {i+1} number"))
    if(num%2!=0):
        a.append(num)
print("----------\n")
a.sort()
for data in a:
    for j in range(1,11):
        print(f"{data} X {j} = {data*j}")
print("---------")

# 2nd way

n = int(input("How many times do you want for multiplication "))
a = []

for i in range(n):
    num = int(input(f"Enter a {i+1} number"))
    if(num%2!=0):
        a.append(num)

a.sort()
for data in a:
    if(data%2!=0):
        for j in range(1,11):
            print(f"{data} X {i} = {data*j}")
