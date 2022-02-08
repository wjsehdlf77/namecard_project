import sqlite3

class NameCard:
    def __init__(self):
        self.book = []

    
    def load(self, FILE_PATH):
        try:
            with open(FILE_PATH, 'rt', encoding='utf-8') as file:
                list = file.readlines()
                for line in list:
                    line = line.strip()
                    self.book.append(line)
                
                return self.book
                    

        except Exception as e:
            print(e)



    def save(self, name):



        con = sqlite3.connect(name)

        cursor = con.cursor()
        cursor.execute("create table tbladdr (name varchar(20), email varchar(30), phone varchar(30), addr text)")

        for ix in self.book:
            element = ix.split(',')
            cursor.execute(f"insert into tbladdr values('{element[0]}', '{element[1]}', '{element[2]}', '{element[3]}')")

        con.commit()

        cursor.close()

        con.close()
