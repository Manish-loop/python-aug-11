# # Lists
# # Values are stored in big brackets
# # Separated by comma 
# # Lists are mutable can be changed

# a = [1, 2, 4, 6]
# print(a)
# print(type(a))

# b = ["ram", 1, 3, 6]
# print(b[0])
# print(b[-1])



# # print(b[5])  Error is IndexError : index out of range



# teachers = ['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil', 'Haris']
# print(teachers[1:4]) # Index 4 ko value katxa
# print(teachers[2:])  # Index 2 dekhi sabai value aauxa
# print(teachers[:5])  # Agadi ko sabai index ko value except 5
# print(teachers[:])   # All values will come
# print(len(teachers)-1) # Total number of index is total length - 1 

# test = [1,2,3, ["anish", "prajapati"]]
# print(test[-1][1]) # this 

# # or this solution
# # value = test[3]
# # print(type(value))
# # print(value[-1])

# # print(test[::])


# # apppend = values added at the end of list
# test.append("hari") # for adding single values
# test.append("subash")
# test.append(["shyam", 1]) # for storing multiple values
# print(test)


print("before append")
a = []
print(a)
print("after append")
a.append(1)
a.append(2)
a.append(3)
a.append(4)

print(a)


# Insert
print("Insert")
test = [1,2,3,4,5]

test.insert(2,"anish")
test.insert(2,"manoj")
test.insert(2,"raj")
test.insert(-1,"easter")
print(test)

a = ["anis","rija","rita"]
b= ["ciza","usha","Raj"]
c = a + b
print(c)


# even bhayo bhane list ma 
# a = int(input("Enter a number: "))
# list = []
# if a % 2 == 0:
#     list.append(a)
# print(list)


# extend 
test = [1,2,3,4,5,6,7,8,9,10]
test2 = ["a","b","c","d"]
test.extend(test2)
print(test)
