from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:33549/AAC' % (username, password))
        # where xxxx is your unique port number
        self.database = self.client['AAC']

    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary  
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Create method to implement the R in CRUD.
    def read(self, data):
        #read = self.database.animals.find(data)  # finds data for Reading
        if data is not None:
            return self.database.animals.find(data)
        else:
            raise Exception("Nothing to read, because data does not exists")

         
    # update method
    def update(self,data):
        if data is not None:
            if data:
                return self.database.animals.update_many(data)
        else:
            raise Exception("Nothing to update")
            
    #delete method
    def delete(self,data):
        if data is not None:
            if data:
                return self.database.animals.delete_one(data)
        else:
            raise Exception("Nothing to Delete")
    