# Guessing a number with number not exceeding count 3 if exceeded display message as limit exceeded

import random 
num = random.randrange(1,10)


count = 0

while True:
    user_num = int(input("Guess a number: "))
    count+=1
    if num == user_num:
        print("Congratulations,guess is correct")
        break
    print("Worng guess")
    if count == 3:
       print("Limit exceeded.")
       break
   
   
# Guess the number 

    
    