<<<<<<< HEAD
  
=======
>>>>>>> e20ea752dcc568b6027624359cf65e908de90720
import pymysql

conn =pymysql.connect(database="db1",user="Aparna",password="123",host="localhost")
cur=conn.cursor()

#create database
#cur.execute("CREATE TABLE users(id int primary, name text, age int, gender text, address text);")

#to store user data

name = "Aparna"
age = 23
gender = "F"
address = "Maharashtra"

data={'name':name,'age':age,'gender':gender,'address':address}
print(data)

# Saving data to DB
cur.execute("INSERT INTO users (name,age,gender,address) VALUES (%(name)s,%(age)s,%(gender)s,%(address)s);",data)
conn.commit()
print("saved to db")

#reading data from DB
cur.execute("SELECT * FROM users;")
#get one row
data1=cur.fetchone()
#get all rows
data2=cur.fetchall()

print(data1)
print(data2)
