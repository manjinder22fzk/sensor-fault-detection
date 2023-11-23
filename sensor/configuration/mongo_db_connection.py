import pymongo
from sensor.constant.database import DATABASE_NAME
import certifi
from urllib.parse import quote_plus

ca = certifi.where()

class MongoDBClient:
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
                
        try:

            if MongoDBClient.client is None:
                username = "manjinder_singh"
                password = "Engineering96@"
                escaped_username = quote_plus(username)
                escaped_password = quote_plus(password)
                MONGO_DB_URL = f"mongodb+srv://{escaped_username}:{escaped_password}@cluster0.ftk5qa5.mongodb.net/?retryWrites=true&w=majority"
                mongo_db_url = MONGO_DB_URL
                print(mongo_db_url)
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e


