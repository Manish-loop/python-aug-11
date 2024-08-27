# syntax

'''
if (condition):
    code block

'''

# single if 
# if (2 == 3):
#     print("It is true")
# else:
#     print("It is false")


# if True:
#     print("This is True")


# a = int(input("Enter first number: "))

# if( a % 2 == 0):
#     print(f"{a} is even")
# else:
#     print(f"{a} is odd")


#  Assignment for calculating percentage
# distinction
# first
# invalid if greater than 100
marks = int(input("Enter marks: "))

if (marks >90):
    print(f"{marks} is A+")   # Python relies on identation(white space at the beginning of line)to define scope of code. Other programming languages often use curly-brackets for this purpose.
elif (marks < 90 and marks >= 80):
    print(f"{marks} is A")
elif (marks < 80 and marks >= 70):
    print(f"{marks} is B+")
elif (marks < 70 and marks >= 60):
    print(f"{marks} is B")
elif(marks < 60 and marks >= 50):
    print(f"{marks} is C+")
else:
    print(f"{marks} is C")
 

