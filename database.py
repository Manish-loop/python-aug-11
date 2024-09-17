import mysql.connector


# db = mysql.connector.connect (
#     host="localhost",
#     user="root"
# )

# print(db)
# try:

#     cursor = db.cursor()
#     cursor.execute("Create Database PythonAUG")
# except:
#     print("Database already exists")
    
    
    
db = mysql.connector.connect (
    host="localhost",
    user="root",
    database="PythonAUG"
)
print(db)
# use try except
cursor = db.cursor()
#cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
cursor.execute("INSERT INTO `customers` (`name`,`address`) VALUES ('broadway','kathmandu');")
db.commit()


