from decouple import config
import pymongo


client = pymongo.MongoClient("mongodb+srv://" + config("MONGO_USERNAME")  + ":" + config("MONGO_PASSWORD") + "@" + config("MONGO_URL") + "/test?retryWrites=true&w=majority")

db = client.crypto
collection = db.cryptocurrencies

print(collection)
