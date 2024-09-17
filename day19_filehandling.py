# a = open("test.py","r")
# print(a.read())


# a = open("sudan.py","w")
# a.write("[1,2,3,4]")
# a.close()

# f = open("test.py","r")

# a = open("sudan.py","w")
# a.write(f.read())
# a.close()




# a = open("sudan.py","w+")
# a.write("I am student")
# a.seek(0)
# c = a.read()
# print(c)


f = open("sudan.py","r+")
print(f.read())
f.write("\nThis is testing from w+")
print(f.read())

#  For creating new file using - x error if already exists
# a = open("test.py","r")
# f = open("sudan.py","x")
# f.create(a.read())
# f.close()




# try:
#    f = open("test.py", "x")
#    print("New file created")
# except:
#     print("Error occured!")



# print(a)


# print(type(a))

# c = int(a)
# print(type(c))



# git reset --hard
# git diff