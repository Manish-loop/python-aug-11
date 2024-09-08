# i = 1 
# n = int(input('Enter number:'))
# while(i<=10):
#     print(f"{n}X{i} = {n*i}")
#     i+=1

# for i in range(1,6):
#     for j in range(1,6):
#         print(i)
#         i+=1

# a = [1,22,33,44]
# sum = 0
# for i in a:
#     sum = sum+i
# print(sum)


# 1. Print Pattern

# Using for loop 
row = 5
for i in range(1,row+1):
    for j in range(1,i+1):
      print(j, end = '')

    print()
print("\n")
# Using while loop
i = 1
while i<=5:
   j = 1
   while j<=i:
     print(j, end='')
     j+=1
   print()
   i+=1



# 2. Calculate sum of all numbers from 1 to a given number
# Write a Python program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
print("\n")
# Using for loop 
print("Sum for for loop")
sum = 0
n = int(input("Enter a number:"))

for i in range(1,n+1):
   sum+= i
print(sum)

print("\n")
# Using while loop
print("Sum for while loop")
sum = 0
n = int(input("Enter number: "))
i = 1
while i<=n:
   sum +=i
   i+=1
print(f"Sum = {sum}")

print("\n")


# # 3. Print Pattern
# # Using for loop
# for x in range(5,0,-1):
#     print("*" * x)

# for y in range(0,6):
#    print("*"*y)
print("For loop star pattern")
for i in range(6,0,-1):
   for j in range(1,i+1):
      print("*", end = "")
      j+=1
   print()
print("\n")

for i in range(1,6):
   for j in range(1,i+1):
      print("*", end = "")
      j+=1
   print()
i+=1




print("\n")

# while loop
print("While loop Star Pattern")
n = 5
i=1
while i<=n:
   j = n
   while j>=i:
      print("*", end="")
      j-=1
   print()
   i+=1


k = 1
while k<=5:
   l = 1
   while l<=k:
       print("*", end ="")
       l+=1
   print()
   k+=1


   

       




