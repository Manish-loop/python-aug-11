# for i in [2,3,5]:
#     print(i)
#     if i == 3:
#         break

# for i in [2,3,5]:
#     if i == 3:
#         break
#     print(i)

# print("continue")
# for i in [2,3,5]:
#     if i == 3:
#         continue
#     print(i) 

# for i in [2,3,5]:
#     print(i) 
#     if i == 3:
#         continue

#using for loop with range(1,6)
# a = []
# for i in range(1,6):
#     a.append(i)
# print(a)


# # list comprehension imp one
# aa = [i for i in range(1,6)]
# print(aa)

# for i in range(1,4):
#     pass               #if for loop with no content and it avoids getting error

# i = 1
# while i<=10:
#     print(i)
#     i+=1

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
