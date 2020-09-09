import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)


mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")

mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)


# Creating a Table
# Make sure you define the name of the database when you create the connection
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# mit Primary Key
# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# ALTER TABLE
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

print("------ TABLES -------")
mycursor.execute("SHOW TABLES")

for tb in mycursor:
    print(tb)

# INSERT
'''
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"

val1 = ("Semra", "Highway 22")
val2 = ("Baran", "Highway 22")

mycursor.execute(sql, val1)
mycursor.execute(sql, val2)

mydb.commit()
'''

# SELECT
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()

for c in myresult:
    print(c)


# WHERE
print("------ WHERE -------")
sql = "SELECT * FROM customers WHERE address ='Highway 22'"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for w in myresult:
    print(w)


# LIKE
print("------ LIKE -------")
sql = "SELECT * FROM customers WHERE address LIKE '%way%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

print("------ Prevent SQL Injection -------")
# Prevent SQL Injection
# Escape query values by using the placeholder %s method:
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Highway 22",)

mycursor.execute(sql, adr)
myresult = mycursor.fetchall()

for r in myresult:
    print(r)


# ORDER BY
print("------ ORDER BY -------")
sql = "SELECT * FROM customers ORDER BY name"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)


# DELETE
# print("------ DELETE -------")
'''
sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
mycursor.execute(sql)
mydb.commit()
'''

# DROP TABLE
'''
sql = "DROP TABLE customers"
mycursor.execute(sql) 
'''

# UPDATE
print("------ UPDATE -------")
sql = "UPDATE customers SET address = 'Baran str. 123' WHERE name = 'Baran'"
mycursor.execute(sql)
mydb.commit()

# LIMIT
print("------ LIMIT -------")
mycursor.execute("SELECT * FROM customers LIMIT 2")
myresult = mycursor.fetchall()
for r in myresult:
    print(r)


# JOINs
'''
users:
{ id: 1, name: 'John', fav: 154},
{ id: 2, name: 'Peter', fav: 154},
{ id: 3, name: 'Amy', fav: 155},
{ id: 4, name: 'Hannah', fav:},
{ id: 5, name: 'Michael', fav:}


products
{ id: 154, name: 'Chocolate Heaven' },
{ id: 155, name: 'Tasty Lemons' },
{ id: 156, name: 'Vanilla Dreams' }
'''

'''
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

mycursor.execute(sql)
myresult = mycursor.fetchall()
for r in myresult:
    print(r)
'''
