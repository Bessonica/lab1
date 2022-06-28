# from psycopg2 import connection
from pymongo import MongoClient


# как создавать коллекции, опредилять ряды и тд
# как отправить новые элементы

dbName = "labrary"
collectionBook = "books"
collectionMagazine = "magazines"

connect_url = "mongodb://root:<password>@<cluster-address>/test?retryWrites=true&w=majority"

client = MongoClient('localhost', 27017)
# db = client.test_database


db = client['library']

# set up insert data
# post = {"name": "000", "genre":"newBookGenre"}
# collectionInput1 = {"name": newBookName, "genre":newBookGenre, "year": newBookYear}


collectionBooks = db.books
collectionMagaz = db.magazines

# collectionMagaz.insert_one(post).inserted_id
# collectionBooks.insert_one(post).inserted_id


# print(post_id)

# name = client.database_name
# print(name.list_database_names())

import sys
sys.path.append('../')