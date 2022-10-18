from time import monotonic
from sensor.configuration.mango_db_connection import MongoDBClient

if __name__=="__main__":
    mongodb_client=MongoDBClient()
    print("collection_name:",mongodb_client.database.list_collection_names())