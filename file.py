def greet(name,dept):
    print(f"hi {name}")
    print(f"Are you from {dept} department?")
    
greet("Jenny",dept="CS")  # This is positional one 


# flatten nested list 
# permutation of list

# b = [1,2,3,4]
# print(type(b))

# print(b[0])
# print(b[-1])

# teachers = ['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil', 'Haris']
# print(teachers[1:4])
# print(teachers[2:])
# print(teachers[:5])
# print(teachers[:])
# teachers.append("Hari")
# print(teachers)


# test = [1,2,3,["Anish", "Prajapati"]]
# print(test[-1][1])
# test.append("manish")
# print(test[-1])
# print(test)

# print("before append")
# a = []
# print(a)
# print("after append")
# a.append(1)
# a.append(2)
# a.append(3)
# a.append(4)
# a.append(5)
# print(a)


test = [1,2,3,4,5]

test.insert(2,"anish")
test.insert(2,"manoj")
print(test)


# a = ["anis","rija","rita"]
# b= ["ciza","usha","Raj"]
# c = a + b
# print(c)


# a = int(input("Enter a number: "))
# list = []

# if a%2 == 0:
#     list.append(a)
# print(list)

test = {
    "name":"Broadway",
    "company": "test",
    "number": [
        {
        "type": 'NTC',
        "mobile":"982345"
    },
    {
          "type": 'Ncell',
        "mobile":"98054"
    }
    ]
}

print(test["number"][0]['type'])
print(test['number'][1]['mobile'])

