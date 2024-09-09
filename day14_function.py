# Function is block of code

# def test():  # It calls function
#     print("This is test")
    
# test() # Function test is called here if not output is not generated

def add():   # Here if return is not used then output generated is None
   data = []
   for i in range(1,5):
       data.append(i)
   return data

print(add())


def myinfo(name):
    print(f"My name is {name}\n")
    
myinfo("Anish")


def detail(name,lname,address,age):
    print(f"My name is {name} {lname}")
    print(f"My address is {address}")
    print(f"My age is {age}")
    print("\n")
    
detail("Hari","Prajapati","Thimi",20)

def kantipur(content,title,author):
    print(title,content,author)
    print("\n")
    
kantipur("war","south","asd")


def kantipur(content,title,author):
    return title,content,author
    
print(kantipur("war","south","asd"))
