# percentage = float(input("Enter percentage: "))

# if(percentage >= 40):
#     print("User is pass")
#     if(percentage >=80):
#         print("User percentage is distinction")
#     elif(percentage>=60):
#         print("First Division")
#     elif(percentage>=55):
#         print("Second Division")
# else:
#     print("Fail")



print("Welcome to the rollercoaster!")
height = float(input("Enter height in cm: "))

if(height>=120 and height<=200):
    print("You can ride rollercoaster.")
    age = int(input("What is yor age? "))
    if age < 12:
        print("PLease pay $5 to ride.")
    elif age<=18:
        print("Please pay $12 to ride.")
    else:
        print("Please pay $15 to ride.")
else:
    print("Sorry, you need to be 120 cm in height to ride rollercoaster.")
     







# gender = "M"
# if (gender == 'M'):
#     print("Gender is male" )
# else:
#     print("Gender is female")
 

#  Single line if 
gender = "M"

a = "Male" if gender == "M" else "female"
print(a)


