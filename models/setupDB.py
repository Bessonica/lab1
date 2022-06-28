import sqlite3
from peewee import *


class dataBaseBooks_Sqlite:
    def __init__(self):
        self.db = sqlite3.connect("books.db")
        self.cursor = self.db.cursor()
        self.createTable()


    def createTable(self):
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS books (id integer PRIMARY KEY AUTOINCREMENT, name text NOT NULL, genre text NOT NULL, year int); """)


    def show(self):
        self.cursor.execute("""SELECT * FROM books """)
        self.rows = self.cursor.fetchall()
        return self.rows

    


class dataBaseMagazines_Sqlite:
    def __init__(self):
        self.dbM = sqlite3.connect("magazines.db")
        self.cursorM = self.dbM.cursor()
        self.createTable()


    def createTable(self):
        self.cursorM.execute(""" CREATE TABLE IF NOT EXISTS magazines (id integer PRIMARY KEY AUTOINCREMENT, title text NOT NULL, issue text NOT NULL, issueTitle text NOT NULL); """)

    def show(self):
        self.cursorM.execute("""SELECT * FROM magazines """)
        self.rows = self.cursorM.fetchall()
        return self.rows


#                                orm part
# 2 класса  Book, magazine
# database_proxy = "books.db"

dbBook = SqliteDatabase('booksORM.db')
dbMagazine = SqliteDatabase('magazinesORM.db')

#  !!!! ті создаешь тейблы в database.py(53 row) , может это принести сюда?

class BaseModelBook(Model):
    id = PrimaryKeyField(unique=True)
    class Meta:
        database = dbBook
        order_by = 'id'

class BaseModelMagazine(Model):
    id = PrimaryKeyField(unique=True)
    class Meta:
        database = dbMagazine
        order_by = 'id'



class Book(BaseModelBook):
    name = CharField()
    genre = CharField()
    year = CharField()

    class Meta:  
        # read about this
        db_table = 'books'
    

class Magazine(BaseModelMagazine):
    title = CharField()
    issue = CharField()
    issueTitle = CharField()

    class Meta:
        # read about this
        db_table = 'magazines'
    



##unfinished method for sqLight management

    # def sqlData_add(self, dataBaseName, arg1, arg2, arg3):
    #     print("deez nuts")
    #     self.database1 = "books"
    #     self.database2 = "magazines"


    #     print("book add args")
    #     print(arg1, arg2, arg3)

    # # зачем этот каунт тут ????
    #     self.cursor.execute("SELECT COUNT(*) from books WHERE name = '" +
    #     arg1 +"' ")
    #     self.result = self.cursor.fetchone()

    # # if dataBaseName == "books":
    # #     pass

    #     if int(self.result[0]) > 0:
    #         print("error")
    #         print(result[0])
    #     elif self.dataBaseName == "books":
    #         self.cursor.execute("INSERT INTO '" + str(database1) +"'(name, genre, year) VALUES(?, ?, ?)", (arg1, arg2, arg3))
    #         self.db.commit()
    #         print("added to books")
    #     elif self.dataBaseName == "magazines":
    #         self.cursorM.execute("INSERT INTO '" + str(database2) +"'(title, issue, issueTitle) VALUES(?, ?, ?)", (arg1, arg2, arg3))
    #         self.dbM.commit()