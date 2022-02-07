from namecard import NameCard
import sqlite3


FILE_PATH = 'addressbook.txt'

book = NameCard()

book.load(FILE_PATH)

count = 0
for element in book.book:
    list_element = list(element.split(','))


conn = sqlite3.connect('addr.db')

cur = conn.cursor()

conn.execute('CREATE TABLE NAMECARD(name varchar(10), email varchar(30), phone varchar(30),addr varchar(30)')

cur.executemany(
    'INSERT INTO NAMECARD VALUES (name, email, phone, addr)',
    
)
    

    

