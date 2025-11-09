
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://chandankumar26102000_db_user:chandu57800@cluster0.ew0ees7.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successf ul connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)