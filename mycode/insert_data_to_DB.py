import sqlite3

myconnection = sqlite3.connect('thisismydb.db')
mycursor = myconnection.cursor()

createitemsquery = "create table if not exists items (itemId INTEGER PRIMARY KEY, name string, price float)"
mycursor.execute(createitemsquery)
items = [
    (1, 'Butter', 23.55),
    (2, 'Honey', 19.42),
    (3, 'Bread', 9.25)
]
insertitemsquery = "insert into items values (?,?,?)"
mycursor.executemany(insertitemsquery, items)

myconnection.commit()
myconnection.close()
