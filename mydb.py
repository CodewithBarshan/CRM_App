import mysql.connector

database=mysql.connector.connect(
    host="localhost",user='root',passwd='Brshubha@1234')

#prepare a cursor object

cursor_object=database.cursor()

#create a database 

cursor_object.execute("CREATE DATABASE barshandb3")
print("Database Created")