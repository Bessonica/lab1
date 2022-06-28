
from tkinter import *
from tkinter import ttk

class GuiTree:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1300x720")

        self.tree = ttk.Treeview(self.window)

        # self.tree['columns'] = ("ID", "Title", "Genre", "Year")


        # self.tree.column("#0", width=0, stretch=NO)
        # self.tree.column("ID", anchor=W, width=100)
        # self.tree.column("Title", anchor=W, width=200)
        # self.tree.column("Genre", anchor=W, width=150)
        # self.tree.column("Year", anchor=W, width=150)

        # self.tree.heading("ID", text="ID", anchor=W)
        # self.tree.heading("Title", text="Title", anchor=W)
        # self.tree.heading("Genre", text="Genre", anchor=W)
        # self.tree.heading("Year", text="Year", anchor=W)


        # self.tree.tag_configure('orow', background='#EEEEEE', font=('Arial bold', 15))
        # self.tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

    def treeReturn(self):
        return self.tree


        

class GuiLabel:
    def __init__(self):

        self.labelBookM1 = Label(text="Enter magazine title")
        self.labelBookM1.place(x = 30, y = 40)
        self.labelBookM1.config(bg='lightgreen', padx = 0)
        self.labelBookM1.grid(row=10, column=0, padx=10, pady=10)

        self.magazineName = Entry(text = "")
        self.magazineName.place(x = 150, y =40, width = 200, height = 25)
        self.magazineName.grid(row= 10, column=1, columnspan=3, padx=2, pady=2)


        self.labelBookM2 = Label(text="Enter magazine issue")
        self.labelBookM2.place(x = 30, y = 70)
        self.labelBookM2.config(bg='lightgreen', padx = 0)
        self.labelBookM2.grid(row=11, column=0, padx=10, pady=10)

        self.magazineIssue = Entry(text = "")
        self.magazineIssue.place(x = 150, y =70, width = 200, height = 25)
        self.magazineIssue.grid(row=11, column=1, columnspan=3, padx=2, pady=2)

        self.labelBookM3 = Label(text="Enter issue title")
        self.labelBookM3.place(x = 30, y = 100)
        self.labelBookM3.config(bg='lightgreen', padx = 0)
        self.labelBookM3.grid(row=12, column=0, padx=10, pady=10)

        self.magazineIssueTitle = Entry(text = "")
        self.magazineIssueTitle.place(x = 150, y = 100, width = 200, height = 25)
        self.magazineIssueTitle.grid(row=12, column=1, columnspan=3, padx=2, pady=2)

    def setUpFunc(self, treemagaz_add, treemagaz_update, treemagaz_delete):
        self.treemagaz_add = treemagaz_add
        self.treemagaz_update = treemagaz_update
        self.treemagaz_delete = treemagaz_delete

        self.buttonAddMag = Button(text = "add magazine", command = treemagaz_add )
        self.buttonAddMag.place(x = 360, y = 60, width = 75, height = 35)
        self.buttonAddMag.grid(row=10, column=4, columnspan=1)
        #edit magazine
        self.buttonEditMag = Button(text = "edit magazine", command = treemagaz_update )
        self.buttonEditMag.place(x = 360, y = 40, width = 75, height = 35)
        self.buttonEditMag.grid(row=11, column=4, columnspan=1)
        #delete magazine
        self.buttonDeleteMag = Button(text = "delete magazine", command = treemagaz_delete )
        self.buttonDeleteMag.place(x = 360, y =20, width = 75, height = 35)
        self.buttonDeleteMag.grid(row=12, column=4, columnspan=1)

        # #buttons
        # # add magazine
        # self.buttonAddMag = Button(text = "add magazine", command = treemagaz_add )
        # self.buttonAddMag.place(x = 360, y = 60, width = 75, height = 35)
        # self.buttonAddMag.grid(row=10, column=4, columnspan=1)
        # #edit magazine
        # self.buttonEditMag = Button(text = "edit magazine", command = treemagaz_update )
        # self.buttonEditMag.place(x = 360, y = 40, width = 75, height = 35)
        # self.buttonEditMag.grid(row=11, column=4, columnspan=1)
        # #delete magazine
        # self.buttonDeleteMag = Button(text = "delete magazine", command = treemagaz_delete )
        # self.buttonDeleteMag.place(x = 360, y =20, width = 75, height = 35)
        # self.buttonDeleteMag.grid(row=12, column=4, columnspan=1)




class GuiLabelM():
    def __init__(self):
        #    enter BOOK NAME
        self.labelBook1 = Label(text="Enter book name")
        self.labelBook1.place(x = 30, y = 40)
        self.labelBook1.config(bg='lightgreen', padx = 0)
        self.labelBook1.grid(row=1, column=0, padx=10, pady=10)

        self.bookName = Entry(text = "")
        self.bookName.place(x = 150, y =40, width = 200, height = 25)
        self.bookName.grid(row=1, column=1, columnspan=3, padx=2, pady=2)

        #    enter BOOK GENRE
        self.labelBook2 = Label(text="Enter book genre")
        self.labelBook2.place(x = 30, y = 70)
        self.labelBook2.config(bg='lightgreen', padx = 0)
        self.labelBook2.grid(row=2, column=0, padx=10, pady=10)

        self.bookGenre = Entry(text = "")
        self.bookGenre.place(x = 150, y =70, width = 200, height = 25)
        self.bookGenre.grid(row=2, column=1, columnspan=3, padx=2, pady=2)

        #  enter BOOK YEAR
        self.labelBook3 = Label(text="Enter book year")
        self.labelBook3.place(x = 30, y = 100)
        self.labelBook3.config(bg='lightgreen', padx = 0)
        self.labelBook3.grid(row=3, column=0, padx=10, pady=10)

        self.bookYear = Entry(text = "")
        self.bookYear.place(x = 150, y = 100, width = 200, height = 25)
        self.bookYear.grid(row=3, column=1, columnspan=3, padx=2, pady=2)


    def setUpFunc(self, treebook_add, treebook_update, treebook_delete):
        self.treebook_add = treebook_add
        self.treebook_update = treebook_update
        self.treebook_delete = treebook_delete


        # add book
        self.buttonAdd = Button(text = "add book", command = treebook_add )
        self.buttonAdd.place(x = 360, y = 60, width = 75, height = 35)
        self.buttonAdd.grid(row=1, column=4, columnspan=1)
        #edit book
        self.buttonEdit = Button(text = "edit book", command = treebook_update )
        self.buttonEdit.place(x = 360, y = 40, width = 75, height = 35)
        self.buttonEdit.grid(row=2, column=4, columnspan=1)
        #delete book
        self.buttonDelete = Button(text = "delete book", command = treebook_delete )
        self.buttonDelete.place(x = 360, y =20, width = 75, height = 35)
        self.buttonDelete.grid(row=3, column=4, columnspan=1)



class GuiCollectionButtonsBook():
    def __init__(self):
        pass


    def setUpFunc(self, collectionAddBook, collectionEditBook, collectionDeleteBook, collectionDisplayBook):
        
        self.collectionAddBook = collectionAddBook
        self.collectionEditBook = collectionEditBook
        self.treemagcollectionDeleteBookaz_delete = collectionDeleteBook
        self.collectionDisplayBook = collectionDisplayBook
        
        # collections   mongo db
        # add to colection
        self.buttonAddToCollBook = Button(text = "add to colection (Book)", command = collectionAddBook )
        self.buttonAddToCollBook.place(x = 360, y =20, width = 75, height = 35)
        self.buttonAddToCollBook.grid(row=15, column=0, columnspan=1)
        # edit element collection
        self.buttonEditCollBook = Button(text = "edit element in colection", command = collectionEditBook )
        self.buttonEditCollBook.place(x = 360, y =20, width = 75, height = 35)
        self.buttonEditCollBook.grid(row=15, column=2, columnspan=1)
        # delete elment collection
        self.buttonDeleteCollBook = Button(text = "delete element in colection", command = collectionDeleteBook )
        self.buttonDeleteCollBook.place(x = 360, y =20, width = 75, height = 35)
        self.buttonDeleteCollBook.grid(row=15, column=3, columnspan=1)
        # display collection  (in console???)
        self.buttonDisplayCollBook = Button(text = "show colection", command = collectionDisplayBook )
        self.buttonDisplayCollBook.place(x = 360, y =20, width = 75, height = 35)
        self.buttonDisplayCollBook.grid(row=15, column=5, columnspan=1)



class GuiCollectionButtonsMagazine():
    def __init__(self):
        pass


    def setUpFunc(self, collectionAddMagazine, collectionEditMagazine, collectionDeleteMagazine, collectionDisplayMagazine):
        
        self.collectionAddMagazine = collectionAddMagazine
        self.collectionEditMagazine = collectionEditMagazine
        self.collectionDeleteMagazine = collectionDeleteMagazine
        self.collectionDisplayMagazine = collectionDisplayMagazine
        
        self.buttonAddToCollMagaz = Button(text = "add to colection (Magazine)", command = collectionAddMagazine )
        self.buttonAddToCollMagaz.place(x = 360, y =20, width = 75, height = 35)
        self.buttonAddToCollMagaz.grid(row=17, column=0, columnspan=1)
        # edit element collection
        self.buttonEditCollMagaz = Button(text = "edit element in colection", command = collectionEditMagazine )
        self.buttonEditCollMagaz.place(x = 360, y =20, width = 75, height = 35)
        self.buttonEditCollMagaz.grid(row=17, column=2, columnspan=1)
        # delete elment collection
        self.buttonDeleteCollMagaz = Button(text = "delete element in colection", command = collectionDeleteMagazine )
        self.buttonDeleteCollMagaz.place(x = 360, y =20, width = 75, height = 35)
        self.buttonDeleteCollMagaz.grid(row=17, column=3, columnspan=1)
        # # display collection  (in console???)
        self.buttonDisplayCollBook = Button(text = "show colection", command = collectionDisplayMagazine )
        self.buttonDisplayCollBook.place(x = 360, y =20, width = 75, height = 35)
        self.buttonDisplayCollBook.grid(row=17, column=5, columnspan=1)






# class GuiBook:
#     def __init__(self):

#         window = Tk()
#         window.geometry("1300x720")
        

#         tree = ttk.Treeview(window)

#         tree['columns'] = ("ID", "Title", "Genre", "Year")

#         tree.column("#0", width=0, stretch=NO)
#         tree.column("ID", anchor=W, width=100)
#         tree.column("Title", anchor=W, width=200)
#         tree.column("Genre", anchor=W, width=150)
#         tree.column("Year", anchor=W, width=150)

#         tree.heading("ID", text="ID", anchor=W)
#         tree.heading("Title", text="Title", anchor=W)
#         tree.heading("Genre", text="Genre", anchor=W)
#         tree.heading("Year", text="Year", anchor=W)


#         tree.tag_configure('orow', background='#EEEEEE', font=('Arial bold', 15))
#         tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

