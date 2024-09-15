# Function is block of code


# def test():  # It calls function  
#     print("This is test")
    
# test() # Function test is called here if not output is not generated

# def add():   # Here if return is not used then output generated is None
#    data = []
#    for i in range(1,5):
#        data.append(i)
#    return data

# print(add())


# def myinfo(name):
#     print(f"My name is {name}\n")
    
# myinfo("Anish")


# def detail(name,lname,address,age):
#     print(f"My name is {name} {lname}")
#     print(f"My address is {address}")
#     print(f"My age is {age}")
#     print("\n")
    
# detail("Hari","Prajapati","Thimi",20)

# def kantipur(content,title,author):
#     print(title,content,author)
#     print("\n")
    
# kantipur("war","south","asd")


# def kantipur(content,title,author):
#     return title,content,author
    
# print(kantipur("war","south","asd"))

# def onlinekhabar(title,content, author="Onlinekhabar admin"):  # default value is always provided at def of function and  default argument should be kept at last 
#     print(title, content, author)
    
# onlinekhabar("test-title", 'tre-content', "sudan")
# onlinekhabar("test-title",'tre-content')



def test(a,b,c):    # maps value according to position  
    print(f"{a},{b},{c}")
    print("hello")
    
test(1,2,3)

print("\n")

def keyword_arg(surname,name):  # maps value according to keywords, it does not care of its position it will give value only according to keywords 
    print(name,surname)
    
keyword_arg(name="sudan",surname="sharma")

print("\n")

def test2(*args):   # positional=> displays all value in tuples  if * is used
    
    sum=0
    for i in args:
        sum+=i
    return sum
    
a = test2(1,2,3,1313)
print(a)
print("\n")

# keywords arguments for **
# arbiratory arguments => it will give value in dictionary

# def test3(**data):
#     print(data)
    
# test3(name="suman",surname="sharma",a = 3)


def test3(**data):  # keywords
    print(data)
    test = list(data)
    return test
    
a = test3(name="suman",surname="sharma",a = 3)
print(a)
    
    
    

def hello(*args, **kwargs):  # arbiratory
    print("positional", args)
    print("keyword",kwargs)
    return args, kwargs

print(hello(1,2,2,3,name="hello"))



# Assignment 
# [1,2,3,[1,2,6,7,8],[3,3]]]
# convert into [1,2,3,1,2,6,7,8,3,3] 
def flatten_list(lst):
    flat_list = []
    
    for item in lst:
        if isinstance(item, list): # The isinstance() function returns True if the specified object is of the specified type, otherwise False
            flat_list.extend(flatten_list(item))  # Recursively flatten and extend
        else:
            flat_list.append(item)  # Append non-list items directly
    
    return flat_list


a = [1, 2, 3, [1, 2, 6, 7, 8], [3, 3]]
flattened = flatten_list(a)
print(flattened)


