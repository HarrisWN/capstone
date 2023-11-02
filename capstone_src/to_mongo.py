from base import Base
import pymongo
import os
from dotenv import load_dotenv
import certifi


class ToMongo(Base):
    def __init__(self):
        Base.__init__(self)
        load_dotenv()
        self.__mongo_url = os.getenv("MONGO_URL")
        self.client = pymongo.MongoClient(self.__mongo_url, tlsCAFile=certifi.where())
        self.db = self.client.db
        self.covid_collection = self.db.covid_collection
        self.df.set_index("time", inplace=True)

    def upload_one_by_one(self):
        for i in self.df.index:
            self.covid_collection.insert_one(self.df.loc[i].to_dict())

    # def upload_collection(self):
    #     self.covid_collection.insert_many([self.df.to_dict()])

    # def drop_collection(self):
    #     self.db.covid_collection.drop()

    # def drop_collection_dynamic(self, col_name: str = "covid_collection"):
    #     self.db.drop_collection(col_name)


if __name__ == "__main__":
    c = ToMongo()
    print("Connection Successful")
    c.upload_one_by_one()
