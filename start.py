
import sys
sys.path.insert(1, './models')

from select import select
from tkinter import *
from tkinter import ttk

from gui import *


from mongoCollection import *

# from gui.py import 

# !!!!!!  DONT FORGET to make database clear every new launch

import sqlite3

from setupDB import dataBaseBooks_Sqlite
from setupDB import dataBaseMagazines_Sqlite

from setupDB import *

# from gui import windowTK

from exportDB import insertSQLightIntoMysql
from exportDB import insertMysqlToPostgreSQL

from setupPostgSQL import *
postSQLDB = dataBasePostg()
postSQLcur = postSQLDB.cur
postSQLcon = postSQLDB.pSQLconn



dbBooks = dataBaseBooks_Sqlite()
dbMagazines = dataBaseMagazines_Sqlite()


from setupMysql import *

from setupMysql import dataBaseBooks_mySQL
mySqlDB = dataBaseBooks_mySQL()

mySQLcur = mySqlDB.mySQLcursor
mySQLcon = mySqlDB.mySQLdb



db = dbBooks.db
cursor = dbBooks.cursor

dbM = dbMagazines.dbM
cursorM = dbMagazines.cursorM



for rows in (Book.select().dicts()):
    Book.get().delete_instance()

for rows in (Magazine.select().dicts()):
    Magazine.get().delete_instance()



collectionBooks.delete_many({})
collectionMagaz.delete_many({})


#   orm setup  start
print("setup PeeWee DB")
print(dbBook.create_tables)
with dbBook:
    dbBook.create_tables([Book])



with dbMagazine:
    dbMagazine.create_tables([Magazine])
# orm setup   end


def reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup



def read(databaseName, tableORM):

    #  ORM PART
    resultORM = []

    # print("READ  ORM  all rows in books")
    if str(tableORM) ==  "<Model: Book>":
        for rows in (tableORM.select().dicts()):
            # print(rows)
            temp = (0, rows['name'], rows['genre'], rows['year'])
            resultORM.append(tuple(temp))
    elif str(tableORM) ==  "<Model: Magazine>":
            for rows in (tableORM.select().dicts()):
                # print(rows)
                temp = (0, rows['title'], rows['issue'], rows['issueTitle'])
                resultORM.append(tuple(temp))
        


    #    SQL PART

    # conn = sqlite3.connect("data.db")
    # cursor = conn.cursor()

    # cursor.execute("""CREATE TABLE IF NOT EXISTS books (id integer PRIMARY KEY AUTOINCREMENT, name text NOT NULL, genre text NOT NULL); """)
    if databaseName == "books":
        cursor.execute("SELECT * FROM books")
        results = cursor.fetchall()
        db.commit()
    elif databaseName == "magazines":
        cursorM.execute("SELECT * FROM magazines")
        results = cursorM.fetchall()
        dbM.commit()


    
    return resultORM
    #return results
    


def readM():
    # Magazine
    cursorM.execute("SELECT * FROM magazines")
    results = cursorM.fetchall()
    # conn.commit()
    dbM.commit()

    resultORM = []
    for rows in (Magazine.select().dicts()):
        # print(rows)
        temp = (0, rows['title'], rows['issue'], rows['issueTitle'])
        resultORM.append(tuple(temp))

    print(resultORM)
    print("   READ M    RESULTS")
    print(results)
    # return results
    return resultORM


#----start   sqlite related   start

def sqlData_add(dataBaseName, arg1, arg2, arg3, tableORM):

    #orm here
    # в таблицу dataBaseName ввести 3 єлемента
    arg1 = str(arg1)
    arg2 = str(arg2)
    arg3 = str(arg3)
    print(str(tableORM))
    if str(tableORM) ==  "<Model: Book>":
        tableORM.create(name = arg1, genre = arg2, year = arg3)
    elif str(tableORM) ==  "<Model: Magazine>":
        tableORM.create(title = arg1, issue = arg2, issueTitle = arg3)

    



    #   clean SQLight below
    print("deez nuts")
    database1 = "books"
    database2 = "magazines"


    print("book add args")
    print(arg1, arg2, arg3)

    # зачем этот каунт тут ????
    cursor.execute("SELECT COUNT(*) from books WHERE name = '" +
    arg1 +"' ")
    result = cursor.fetchone()


    if int(result[0]) > 0:
        print("error")
        print(result[0])
    elif dataBaseName == "books":
        cursor.execute("INSERT INTO '" + str(database1) +"'(name, genre, year) VALUES(?, ?, ?)", (arg1, arg2, arg3))
        db.commit()
        print("added to books")
    elif dataBaseName == "magazines":
        cursorM.execute("INSERT INTO '" + str(database2) +"'(title, issue, issueTitle) VALUES(?, ?, ?)", (arg1, arg2, arg3))
        dbM.commit()


def sqlData_delete(deleteObject, deleteID, databaseName, tableORM):

    #  ORM part
    # deleteObject id, name, genre, year

    
    print(str(tableORM))
    print(deleteObject)
    if str(tableORM) ==  "<Model: Book>":
        rowToDelete = tableORM.get(tableORM.name == str(deleteObject[1]))
        print("row to delte ORM")
        print(rowToDelete)
        rowToDelete.delete_instance()
    elif str(tableORM) ==  "<Model: Magazine>":
        rowToDelete = tableORM.get(tableORM.title == str(deleteObject[1]))
        print("row to delte ORM")
        print(rowToDelete)
        rowToDelete.delete_instance()
        
        


    #  sql part
    #find book in db by id
    if databaseName == "books":
        cursor.execute("DELETE FROM books WHERE id = '" + str(deleteID) + "'")
        db.commit()
    elif databaseName == "magazines":
        cursorM.execute("DELETE FROM magazines WHERE id = '" + str(deleteID) + "'")
        dbM.commit()
  

    
def sqlData_edit(updatObject, updateID, databaseName, arg1, arg2, arg3, tableORM):
    print("updated ID")
    print(updateID)

    arg1 = str(arg1)
    arg2 = str(arg2)
    arg3 = str(arg3)
    # editBookID = bookID.get()

    # conn = sqlite3.connect("books.db")
    # cursor = conn.cursor()

    
    print(str(tableORM))
    print(updatObject)
    if str(tableORM) ==  "<Model: Book>":
        rowToEdit = tableORM.get(tableORM.name == str(updatObject[1]))

        rowToEdit.name = arg1
        rowToEdit.genre = arg2
        rowToEdit.year = arg3
        rowToEdit.save()
       # rowToEdit.update({rowToEdit.name:arg1, rowToEdit.genre: arg2, rowToEdit.year: arg3 })
        
    elif str(tableORM) ==  "<Model: Magazine>":
        rowToEdit = tableORM.get(tableORM.title == str(updatObject[1]))

        rowToEdit.title = arg1
        rowToEdit.issue = arg2
        rowToEdit.issueTitle = arg3
        rowToEdit.save()
        print("row to delte ORM")
        print(rowToEdit)
        

    if databaseName == "books":
        cursor.execute("UPDATE books SET name = '" + str(arg1) + "', genre = '" + str(arg2) + "', year = '" + str(arg3) + "' WHERE id ='" + str(updateID) + "'")
        db.commit()
    elif databaseName == "magazines":
        cursorM.execute("UPDATE magazines SET title = '" + str(arg1) + "', issue = '" + str(arg2) + "', issueTitle = '" + str(arg3) + "' WHERE id ='" + str(updateID) + "'")
        dbM.commit()

    # cursor.execute("UPDATE books SET name = '" + str(editBookName) + "', genre = '" + str(editBookGenre) + "', year = '" + str(editBookYear) + "' WHERE id ='" + str(updateID) + "'")
    # db.commit()


# cursor.execute("UPDATE inventory SET itemId = '" "', itemName = '" + str(name) + "', itemPrice = '" + str(price) + "', itemQuantity = '" + str(quantity) + "' WHERE itemId='"+str(idName)+"'")

# ----end   sqlite related   


#----start   tree related
def treebook_add():

    newBookName = labelM.bookName.get()
    newBookGenre = labelM.bookGenre.get()
    newBookYear = labelM.bookYear.get()

    # here we give database name
    sqlData_add("books", newBookName, newBookGenre, newBookYear, Book)


    #  why this part here????
    for data in tree.get_children():
        tree.delete(data)


    for result in reverse(read("books", Book)):
        tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")


def treebook_update():
    selected_item = tree.selection()[0]
    updateID = tree.item(selected_item)['values'][0]
    updatObject = tree.item(selected_item)['values']
    
    editBookName = labelM.bookName.get()
    editBookGenre = labelM.bookGenre.get()
    editBookYear = labelM.bookYear.get()
    sqlData_edit(updatObject, updateID, "books", editBookName, editBookGenre, editBookYear, Book)

      # update tree
    for data in tree.get_children():
        tree.delete(data)


    for result in reverse(read("books", Book)):
        tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    
    


def treebook_delete():
    selected_item = tree.selection()[0]
    deleteID = tree.item(selected_item)['values'][0]
    deleteObject = tree.item(selected_item)['values']
    print("delete ID")
    print(deleteObject)
    sqlData_delete(deleteObject, deleteID, "books", Book)

          # update tree
    for data in tree.get_children():
        tree.delete(data)


    for result in reverse(read("books", Book)):
        tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    
#     MAGAZINE PART
def treemagaz_add():
    newMagazTitle = labels.magazineName.get()
    newMagazIssue = labels.magazineIssue.get()
    newMagazIssueTitle = labels.magazineIssueTitle.get()
    dataBaseName = "magazines"

    print("magaz data")
    print(newMagazTitle, newMagazIssue, newMagazIssueTitle)
    sqlData_add(dataBaseName, newMagazTitle, newMagazIssue, newMagazIssueTitle, Magazine)

    for data in treeMagaz.get_children():
        treeMagaz.delete(data)


    for result in reverse(read("magazines", Magazine)):
        treeMagaz.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")



def treemagaz_update():
    selected_item = treeMagaz.selection()[0]
    updateID = treeMagaz.item(selected_item)['values'][0]
    print(updateID)
    updatObject = treeMagaz.item(selected_item)['values']

    newMagazTitle = labels.magazineName.get()
    newMagazIssue = labels.magazineIssue.get()
    newMagazIssueTitle = labels.magazineIssueTitle.get()
    dataBaseName = "magazines"
    sqlData_edit(updatObject, updateID, "magazines", newMagazTitle, newMagazIssue, newMagazIssueTitle, Magazine)


    for data in treeMagaz.get_children():
        treeMagaz.delete(data)


    for result in reverse(read("magazines", Magazine)):
        treeMagaz.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")


    

def treemagaz_delete():
    selected_item = treeMagaz.selection()[0]
    deleteID = treeMagaz.item(selected_item)['values'][0]
    deleteObject = treeMagaz.item(selected_item)['values']
    sqlData_delete(deleteObject, deleteID, "magazines", Magazine)

          # update tree
    for data in treeMagaz.get_children():
        treeMagaz.delete(data)


    for result in reverse(read("magazines", Magazine)):
        treeMagaz.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    


#----end   tree related


#   collection  mongoDB    start

def collectionAdd(arg1, arg2, arg3, collection):    
    #  collection    в book или magazine?
    newBookName = str(arg1)
    newBookGenre = str(arg2)
    newBookYear = str(arg3)
    print("collections")
    print(newBookName, newBookGenre, newBookYear)
    if(collection == "book"):
        collectionInput1 = {"name": newBookName, "genre":newBookGenre, "year": newBookYear}
        collectionBooks.insert_one(collectionInput1).inserted_id
    else:
        collectionInput1 = {"title": newBookName, "issue":newBookGenre, "issueTitle": newBookYear}
        collectionMagaz.insert_one(collectionInput1).inserted_id




    collectionInput1 = {"name": newBookName, "genre":newBookGenre, "year": newBookYear}
    collectionInput2 = {"title": newBookName, "issue":newBookGenre, "issueTitle": newBookYear}
    

    # newBookName = str(bookName.get())
    # newBookGenre = str(bookGenre.get())
    # newBookYear = str(bookYear.get())

def collectionEdit(arg1, arg2, arg3, collectionName):
    #find by name and change it
    arg1 = str(arg1)
    arg2 = str(arg2)
    arg3 = str(arg3)
    print("  COLLECTION YO")
    print(arg1, arg2, arg3)
    if (collectionName == "book"):
        edit = collectionBooks.find_one({ "name": arg1 })
        print("collection edit")
        print(edit)
        collectionBooks.update_one({ "name": arg1 }, {
           "$set":{ "genre": arg2, "year": arg3}
        })
    elif (collectionName == "magazine"):
        collectionMagaz.update_one({ "title": arg1 }, {
           "$set":{ "issue": arg2, "issueTitle": arg3}
        })
    
def collectionDelete(arg1, collectionName):
    arg1 = str(arg1)
    print(" DELETE ELEMENT IN COLECTION MAGAZINE")
    print(arg1)

    if (collectionName == "book"):
        print("book")
        collectionBooks.delete_one({"name": arg1})
    elif (collectionName == "magazine"):
        print(" collectionName == magazine")
        collectionMagaz.delete_one({"name": arg1})


def collectionAddBook():
    collectionAdd(labelM.bookName.get(), labelM.bookGenre.get(), labelM.bookYear.get(), "book")

def collectionAddMagazine():
    collectionAdd(labels.magazineName.get(), labels.magazineIssue.get(), labels.magazineIssueTitle.get(), "magazine")

def collectionEditBook():
    collectionEdit(labelM.bookName.get(), labelM.bookGenre.get(), labelM.bookYear.get(), "book")

def collectionEditMagazine():
    collectionEdit(labels.magazineName.get(), labels.magazineIssue.get(), labels.magazineIssueTitle.get(), "magazine")


def collectionDeleteBook():
    collectionDelete(labelM.bookName.get(), "book")
    

def collectionDeleteMagazine():
    collectionDelete(labels.magazineName.get(), "magazine")

    
def collectionDisplayBook():
    find = collectionBooks.find()
    print("___ collection:  Books _____")
    for docum in find:
        print("Name: " + docum["name"] + "  genre: " + docum["genre"] + " year: " + docum["year"])

    print("___ End of collection:  Books _____")
   
    

def collectionDisplayMagazine():
    find = collectionMagaz.find()
    print(find)
    print("___ collection:  Magazine _____")
    for docum in find:
        print("title: " + docum["title"] + "  issue: " + docum["issue"] + " year: " + docum["issueTitle"])


    print("___ End of collection:  Magazine _____")
    


#   collection  mongoDB    end



window = GuiTree().window




#   !!!!
tree = ttk.Treeview(window)



# tree = GuiTree().tree

tree['columns'] = ("ID", "Title", "Genre", "Year")

tree.column("#0", width=0, stretch=NO)
tree.column("ID", anchor=W, width=100)
tree.column("Title", anchor=W, width=200)
tree.column("Genre", anchor=W, width=150)
tree.column("Year", anchor=W, width=150)

tree.heading("ID", text="ID", anchor=W)
tree.heading("Title", text="Title", anchor=W)
tree.heading("Genre", text="Genre", anchor=W)
tree.heading("Year", text="Year", anchor=W)


tree.tag_configure('orow', background='#EEEEEE', font=('Arial bold', 15))
tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)



# magazine tree
treeMagaz = ttk.Treeview(window)

treeMagaz['columns'] = ("ID", "Title", "Issue", "Issue title")

treeMagaz.column("#0", width=0, stretch=NO)
treeMagaz.column("ID", anchor=W, width=100)
treeMagaz.column("Title", anchor=W, width=200)
treeMagaz.column("Issue", anchor=W, width=150)
treeMagaz.column("Issue title", anchor=W, width=150)

treeMagaz.heading("ID", text="ID", anchor=W)
treeMagaz.heading("Title", text="Title", anchor=W)
treeMagaz.heading("Issue", text="Issue", anchor=W)
treeMagaz.heading("Issue title", text="Issue title", anchor=W)

treeMagaz.tag_configure('orow', background='#EEEEEE', font=('Arial bold', 15))
treeMagaz.grid(row=10, column=5, columnspan=4, rowspan=5, padx=10, pady=10)


#      READ DATA from tables and add to tree

#upddate magazine tree
for data in treeMagaz.get_children():
    treeMagaz.delete(data)

for result in reverse(read("magazines", Magazine)):
    treeMagaz.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")



    
        #upddate book tree
for data in tree.get_children():
    tree.delete(data)

for result in reverse(read("books", Book)):
    tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

        

# gui part
labels = GuiLabel()
labels.setUpFunc(treemagaz_add,treemagaz_update, treemagaz_delete)


labelCollectionBook = GuiCollectionButtonsBook()
labelCollectionBook.setUpFunc(collectionAddBook, collectionEditBook, collectionDeleteBook, collectionDisplayBook)


labelCollectionMagazine = GuiCollectionButtonsMagazine()
labelCollectionMagazine.setUpFunc(collectionAddMagazine, collectionEditMagazine, collectionDeleteMagazine, collectionDisplayMagazine)





def exportSQLight():
    insertSQLightIntoMysql(dbBooks, dbMagazines,mySQLcur, mySQLcon, Book, Magazine, Book1, Magazine1)
    

def exportMySQL():
    insertMysqlToPostgreSQL(mySqlDB, postSQLcur, postSQLcon, Book1, Magazine1, BookpSQL, MagazinepSQL)
    

buttonExportSQLightTomySQL = Button(text = "aSQLight to MYsql", command = exportSQLight )
buttonExportSQLightTomySQL.place(x = 360, y = 60, width = 75, height = 35)
buttonExportSQLightTomySQL.grid(row=10, column=10, columnspan=1)

buttonExportMySQLToPostgreSQL = Button(text = "mySQL to postgreSQL ", command = exportMySQL )
buttonExportMySQLToPostgreSQL.place(x = 360, y = 60, width = 75, height = 35)
buttonExportMySQLToPostgreSQL.grid(row=11, column=10, columnspan=1)



labelM = GuiLabelM()
labelM.setUpFunc(treebook_add, treebook_update, treebook_delete)



for data in treeMagaz.get_children():
    treeMagaz.delete(data)

for data in tree.get_children():
    tree.delete(data)
#-----END     GUI

window.mainloop()




read("books", Book)