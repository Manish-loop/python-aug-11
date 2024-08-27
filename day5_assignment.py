# n1 = int(input("Enter marks in English: "))
# n2 = int(input("Enter marks in Maths: "))
# n3 = int(input("Enter marks in Nepali: "))
# n4 = int(input("Enter marks in Science: "))

# total = n1+n2+n3+n4
# print(type(total))
# percentages = total/4

# _percentages= float(input("Enter percentage: "))  // It is best to use underscore(_) while defining variables
# if(_percentages >= 80 and _percentages <= 100):
# print(f"{_percentages} is distinction.")


percentages = float(input("Enter percentage: "))

if(percentages >= 80 and percentages <= 100):
    print(f"{percentages} is distinction.")

elif(percentages >= 60 and percentages < 80):
    print(f"{percentages} is first division.")
elif(percentages >=50 and percentages < 60):
    print(f"{percentages} is second division.")
elif(percentages >=45 and percentages < 50):
    print(f"{percentages} is third division")
elif(percentages < 45 and percentages >= 0):
    print(f"Person with {percentages} is failed.")
else:  
    print(f"{percentages} is invalid.")