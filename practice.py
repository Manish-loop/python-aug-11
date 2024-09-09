# Guessing a number with number not exceeding count 3 if exceeded display message as limit exceeded

import random 
num = random.randrange(1,10)

count = 0
 
while True:
    user_num = int(input("Guess the number: "))
    count+=1
    if num == user_num:
        print("Congratualtion, correct guess.")
        break
    if count == 3:
        print("Limit reached")
        break
    
    
    print("Wrong guess")



# Guess number with number of attempts to correct guess

import random 
num = int(input("Guess the number: "))
count = 0

while True:
     user_num = int(input("Guess the number: "))
     count+=1
     
     if num == user_num:
         print(f"Congralutaions, guess is in {count} attempts.") 
         break
     
     
     print("Wrong guess")
     
    