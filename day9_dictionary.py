# dictionary = {} and (key and value) ==> pair 
#  This is mutable can be changed

# stu = {
#     'name': "Manish",
#     'surname': "Prajapati",
#     'roll' : 9, 
#      'address':["dang",'Kathmandu'],
#     'sub' : {
#         "phy": 90,
#     },
   
# }

# print(stu)
# print(stu['name'])
# print(stu['sub']['phy'])
# print(stu['roll'])
# print(stu['address'][-1])


# print(stu.get('middle_name','-'))


# # get all keys from dict

# print(stu.keys())
# print(stu.values())

# print(len(stu))


# # add key and value in dict = value upadate or create new one 
# stu['broadway'] = 'python'
# stu['address'] = 'sudan'
# print(stu)

# bit warden = password saving
# register .com.np



# stu['test'] = "testing value"
# print(stu)
# print(len(stu))


# test = {
#     "name":"Broadway",
#     "company": "test",
#     "number": {
#         "type": 'NTC',
#         "mobile":"982345"
#     }
# }

# print(test['number']['type'])
# print(test.keys())
# print(test.values())


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

print(test['number'][0]['type'])
print(test['number'][1]['type'])

test.update({"name":"sudan","number": 1,"test": "testing"})
print(test)

# del test["number"]
# print(test)

# del test  # Here test variable is deleted
# print(test)
  
test = {
    "name":"Broadway",
    "company": "test",
    "number": 123
    
}
tt = test.pop("number")
print(test)
print(tt)


test.popitem()
print(test)

