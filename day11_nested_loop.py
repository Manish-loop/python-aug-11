# nested for loop

# for i in [1,2]:
#     for j in [3,4]:
#         print(i,j)

# for i in [1,2]:
#     for j in [3,4]:
#         print(i,j)
#         for ij in [5,6]:
#             print(i,j,ij)

# Using nested loop find multiplication table of a = [2,3,5]
# Multiplication Table
a = [2,3,5]
for i in a:
    for j in range(1,11):
        print(f" {i} X {j} = {i*j}")
    print("\n")

    