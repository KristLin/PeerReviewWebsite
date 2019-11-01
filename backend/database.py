from pymongo import MongoClient
from bson import ObjectId
from random import sample

# import os
# from dotenv import load_dotenv

# Database to manipulate user & house data
# load_dotenv()
# DB_PASSWORD = os.getenv("DB_PASSWORD")


class DB(object):
    def __init__(self):

        # connect to local mongoDB
        self.dbclient = MongoClient('mongodb://localhost:27017/')
        self.db = self.dbclient['9323DB']
        self.users = self.db['users']
        self.projects = self.db['projects']
        self.files = self.db['files']

        # connect to mongoDB Atlas
        # self.dbclient = MongoClient(f'mongodb://krist:krist@9900-cluster-shard-00-00-ljnr8.mongodb.net:27017,9900-cluster-shard-00-01-ljnr8.mongodb.net:27017,9900-cluster-shard-00-02-ljnr8.mongodb.net:27017/test?ssl=true&replicaSet=9900-cluster-shard-0&authSource=admin&retryWrites=true&w=majority',  maxPoolSize=50, connect=False)
        # self.users = self.dbclient.airbnbDB.users
        # self.houses = self.dbclient.airbnbDB.houses
        # self.savelists = self.dbclient.airbnbDB.savelists
        # self.comments = self.dbclient.airbnbDB.comments

        # connect to mongoDB mlab

        # self.dbclient = MongoClient(
        #     f"mongodb://krist123:{DB_PASSWORD}@ds335678.mlab.com:35678/9900-database",
        #     123456,
        # ).get_default_database()
        
        # self.dbclient = MongoClient(
        #     f"mongodb://krist123:{DB_PASSWORD}@ds045679.mlab.com:45679/bomb-shrimper",
        #     123456,
        # ).get_default_database()
        # self.users = self.dbclient["users"]
        # self.houses = self.dbclient["houses"]
        # self.savelists = self.dbclient["savelists"]
        # self.comments = self.dbclient["comments"]
        
        super().__init__()

    # =========== user data manipulation ===========
    def find_user_by_id(self, user_id):
        found_user = self.users.find_one({"_id": ObjectId(user_id)})
        if found_user:
            found_user["_id"] = str(found_user["_id"])
        return found_user

    def find_user_by_email(self, email):
        found_user = self.users.find_one({"email": email})
        if found_user:
            found_user["_id"] = str(found_user["_id"])
        return found_user

    def find_all_users(self):
        cursor = self.users.find()
        all_users = []
        for user in cursor:
            user["_id"] = str(user["_id"])
            all_users.append(user)
        return all_users

    def add_user(self, user):
        _id = str(self.users.insert_one(user).inserted_id)
        return _id

    # update & delete need to return a flag
    def update_user(self, user_id, update_info):
        query = {"_id": ObjectId(user_id)}
        return self.users.update_one(query, {"$set": update_info})

    def update_user_profile(self, user_id, update_profile):
        query = {"_id": ObjectId(user_id)}
        return self.users.update_one(query, {"$set": {"profile": update_profile}})

    def delete_user(self, user_id):
        self.users.delete_one({"_id": ObjectId(user_id)})

    # =========== project data manipulation ===========
    def find_project_by_id(self, project_id):
        found_project = self.projects.find_one({"_id": ObjectId(project_id)})
        if found_project:
            found_project["_id"] = str(found_project["_id"])
        return found_project

    def find_all_projects(self):
        cursor = self.projects.find()
        all_projects = []
        for project in cursor:
            project["_id"] = str(project["_id"])
            all_projects.append(project)
        return all_projects

    def add_project(self, project):
        _id = str(self.projects.insert_one(project).inserted_id)
        return _id

    # =========== file data manipulation ===========
    def find_file_by_id(self, project_id):
        found_file = self.files.find_one({"_id": ObjectId(file_id)})
        if found_file:
            found_file["_id"] = str(found_file["_id"])
        return found_file

    def find_all_files(self):
        cursor = self.files.find()
        all_files = []
        for file in cursor:
            file["_id"] = str(file["_id"])
            all_files.append(file)
        return all_files
    
    def add_file(self, file):
        _id = str(self.files.insert_one(file).inserted_id)
        return _id