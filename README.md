# lab 2-3 project 
information system for library

we have books and magazines table
## Books:
 - name, genre, year

## Magazines:
 - title, issue, issueTitle

We have to export 3 rows from sqlite into mySQL database and export 2 rows into postgSQL (17 вариант)

### Screenshot examples are down bellow

package used, used virtual env:
- mysql-connector==2.2.9
- mysql-connector-python==8.0.29
- peewee==3.15.0
- protobuf==4.21.2
- psycopg2==2.9.3
- pymongo==4.1.1
- PyMySQL==1.0.2

start program from start.py( python start.py )

## what changed
1. replaced all sql related code to ORM (peewee)
2. added sepparate local collection noSQL with pymongo
3. separated some of the gui **(gui.py)**
- we have classes: GuiTree, GuiLabel(for magazine tree) GuiLabelM(for book tree)
- GuiCollectionButtonsBook, GuiCollectionButtonsMagazine (for noSQL collection)
4. DB for ORM in sepparate files
- sqLight ( booksORM.db, magazinesORM.db ) 
- mySQL db - **test1**  tables - **books1**  **magazines1**
- postgreSQL db - **test1**   tables -  **BookpSQL** **MagazinepSQL**


## NoSQL
You have options to add, delete, show in console and update elements in collection
- setup in **mongoCollection.py**
- methods - collectionAdd, collectionEdit, collectionDelete, collectionDisplayBook, collectionDisplayMagazine
- you can delete, or edit elments by specifing **right name**
(you can edit everything except name)

## SQLight
We have two sqLight databases (dataBaseBooks_Sqlite, dataBaseMagazines_Sqlite).They are created in **setupDB.py file**
- names of db:  magazines.db, books.db
Each one of them have 1 table.(books, magazines)
- you can create, deleat, update, display **(CRUD)**
- to delete and edit you have **TO** **CHOOSE** row from table? change what you want and then press delete/update button

## mySQL
mySQL database (dataBaseBooks_mySQL) from **setupMysql.py**
- name: test1
- tables: (books1, magazines1)

constructor has method to create table and to drop all rows(it is made
so rows would not duplicate, when launch again):
- createTableBooks, createDataBase
- dropTableMagazines1, dropTableBooks1

## postgreSQL
in postgreSQL we have database test. **setupPostgSQL.py**
- name: test
- tables: (books1, magazines1)

## functions in start.py
1. function, responsible for SQLight -> mySQL:  **insertSQLightIntoMysql** 
2. function, responsible for mySQL -> postgreSQL: **insertMysqlToPostgreSQL**
3. you can find them in file (exportDB.py)


functions, responsible for tree management 
- treebook_***  (add, update, delete)
- treemagaz_*** (add, update, delete))

# Screenshots
dont forget to add them


# Example screenshots


![alt text](https://github.com/[username]/[reponame]/blob/[branch]/image.jpg?raw=true)


## add data to sqLight
![alt text](images/addData.png)
## export it to mSQL, postgreSQL

### mySQL
![alt text](images/mySQL.png)
![alt text](images/mySQL1.png)

### postgreSQL
![alt text](images/pSQL.png)
![alt text](images/pSQL1.png)

## added data to collections
![alt text](images/collection.png)

### displayed collection
![alt text](images/collection1.png)


## added and edited  data
![alt text](images/collection2.png)