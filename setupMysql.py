import mysql.connector

import pymysql
from peewee import *

# connect, create database  done
# connect with orm and make tables   done

 
#   orm part    start
dbmySQLorm = MySQLDatabase('test1', user = 'root', password = 'agoptq', host = 'localhost')

            # host='localhost',
            # user='root',
            # password='agoptq',
            # auth_plugin='mysql_native_password',
            # database = 'test'

class BaseModel(Model):
    id = PrimaryKeyField(unique=True)
    class Meta:
        database = dbmySQLorm
        order_by = 'id'


class Book1(BaseModel):
    name = CharField()
    genre = CharField()
    year = CharField()

    class Meta:  
        # read about this
        db_table = 'books1'
    


class Magazine1(BaseModel):
    title = CharField()
    issue = CharField()
    issueTitle = CharField()

    class Meta:
        # read about this
        db_table = 'magazines1'


# dbmySQLorm.connect()
# dbmySQLorm.create_tables([Book1, Magazine1])
    

#  orm part   end

#    sql part
#  this db has both tables 

class dataBaseBooks_mySQL:
    def __init__(self):
        self.mySQLdb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='agoptq',
            auth_plugin='mysql_native_password',
            database = 'test'
        )
        self.mySQLcursor = self.mySQLdb.cursor()
        #   dont forget about create table !!!!


    def createDataBase(self):
        self.mySQLcursor.execute("CREATE DATABASE test")

    def createTableBooks(self):
        self.mySQLcursor.execute("CREATE TABLE books1 (name VARCHAR(255), genre VARCHAR(255), year VARCHAR(255), book_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
        

    def createTableMagazines(self):
        self.mySQLcursor.execute("CREATE TABLE magazines1 (name VARCHAR(255), genre VARCHAR(255), year VARCHAR(255), book_id INTEGER AUTO_INCREMENT PRIMARY KEY)")

    def showBooks(self):
        self.mySQLcursor.execute("SELECT * FROM books1")
        self.rows = self.mySQLcursor.fetchall()
        return self.rows
        

    def showMagazines(self):
        self.mySQLcursor.execute("SELECT * FROM magazines1")
        self.rows = self.mySQLcursor.fetchall()
        return self.rows





# mySQLdb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='agoptq',
#     auth_plugin='mysql_native_password',
#     database = 'test1'
# )
# mySQLcursor = mySQLdb.cursor()

# conn = pymysql.connect(host='localhost', user='root', password='agoptq')
# conn.cursor().execute('CREATE DATABASE test1')
# conn.close()





# # create DB
# mySQLcursor.execute("CREATE DATABASE test1")

#name, genre, year
# create table
#mySQLcursor.execute("CREATE TABLE books (name VARCHAR(255), genre VARCHAR(255), year INTEGER(10), book_id INTEGER AUTO_INCREMENT PRIMARY KEY)")