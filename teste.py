import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="bonis",
  database="teste"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM pet;")

for x in mycursor:
  print(x)