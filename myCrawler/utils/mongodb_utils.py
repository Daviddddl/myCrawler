import pymongo
from myCrawler.settings import MONGODB_HOST
from myCrawler.settings import MONGODB_PORT

connection = pymongo.MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
tdb = connection.dinning_menu
post_info = tdb.menu

print(MONGODB_HOST)

def insert_data(data):
    post_info.insert(data)

def remove_data(data):
    post_info.remove(data)
