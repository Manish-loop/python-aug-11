# import random

# a = random.random() #  float value between 0 and 1
# print(a)

# b = random.randrange(100,400) # range of values any number to any number
# print(b)



#  Guess a number and compare it with random number and calculate number of attempt

# import random
# num = random.randrange(1,10)
# print(num)

# add = 0 
# while True:
  
#   user_num = int(input("Guess the number: "))
#   add+=1
#   if(num==user_num):
#     print(f"Congratulations, correct guess in {add} attempts.")
#     break
 
#   print("Wrong guess")
 
 # Hit miss assignment
# import random 
# num = random.randrange(0,1)
# print(num)
# score = 100

# while True:
#   if num%2 == 0:
#     print("hit")
#     score +=10
#     print(f"Score is {score}")
#     if score <100:
#      print("Exit")
#      break
#   else:
#     print("Miss")
#     score -=20
#     print(f"Score is {score}")

import random

score = 100
num = random.randint(1, 10)  # Generate a random number 0 or 1
count = 0
while True:  # Infinite loop
    
    count += 1
    user_num = int(input("Guess number: "))
    if num == user_num:
        print("hit")
        score += 10
        print(f"Score is {score} in {count} attempts")
        if score >=200:
            print(f"Congratulations you are winner with {score} score in {count} attempts.")
        break
    if count >8:
        print("Exit")
        break
       
    else:
        print("Miss")
        score -= 20
        print(f"Score is {score}")
    if score < 100:
            print("Exit")
            break  # Exit the loop
print(num)

   








