import pymongo
CONNECTION_STRING = "mongodb+srv://basbusa:16456145@cluster0.jvols.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = db = client.get_database('Moviesproject')
user_collection = pymongo.collection.Collection(db, 'Posters')

for x in user_collection.find():
    print(x)
##just for testing  style="background-image: url({{ url_for('static', filename='posterbg2.jpg') }})" style="background-repeat: no-repeat;
