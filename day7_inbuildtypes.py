# Lists
# Values are stored in big brackets
# Separated by comma 
# Lists are mutable can be changed

a = [1, 2, 4, 6]
print(a)
print(type(a))

b = ["ram", 1, 3, 6]
print(b[0])
print(b[-1])



# print(b[5])  Error is IndexError : index out of range



teachers = ['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil', 'Haris']
print(teachers[1:4]) # Index 4 ko value katxa
print(teachers[2:])  # Index 2 dekhi sabai value aauxa
print(teachers[:5])  # Agadi ko sabai index ko value except 5
print(teachers[:])   # All values will come
print(len(teachers)-1) # Total number of index is total length - 1 

test = [1,2,3, ["anish", "prajapati"]]
print(test[-1][1]) # this 

# or this solution
# value = test[3]
# print(type(value))
# print(value[-1])

# print(test[::])


# apppend = values added at the end of list
test.append("hari") # for adding single values
test.append("subash")
test.append(["shyam", 1]) # for storing multiple values
print(test)