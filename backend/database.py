from pymongo import MongoClient
from bson import ObjectId
from random import sample

# ======= data models start =======
# user: {
#     "_id": ObjectId,
#     "email": String,
#     "name": String,
#     "password": String,
#     "major": String,
#     "createdTime": String,
#     "commentNum": Integer,
#     "likedNum": Integer,
#     "topNum": Integer,
#     "points": Integer,
# }
# 
# project: {
#     "_id": ObjectId,
#     "user": String,
#     "major": String,
#     "title": String,
#     "description": String,
#     "createdTime": String,
#     "isOnTop": Boolean,
#     "isOnTopTime": String,
# }
# 
# file: {
#     "_id": ObjectId,
#     "project": String,
#     "user": String,
#     "title": String,
#     "content": String,
#     "createdTime": String,
#     "rating": Float,
#     "ratingNum": Integer
# }
# 
# comment: {
#     "_id": ObjectId,
#     "file": String,
#     "user": String,
#     "userName": String,
#     "content": String,
#     "rating": Integer,
#     "createdTime": String,
#     "likedNum": Integer
# }
# 
# like: {
#     "_id": ObjectId,
#     "comment": String,
#     # user who liked the comment
#     "user": String,
# }
# ======= data models end =======


# Database to manipulate user & house data
class DB(object):
    def __init__(self):
        # connect to mongoDB mlab
        self.dbclient = MongoClient(f"mongodb://krist123:krist123@ds141188.mlab.com:41188/9323-project", 123456,).get_default_database()
        # declare collections
        self.users = self.dbclient["users"]
        self.projects = self.dbclient["projects"]
        self.files = self.dbclient["files"]
        self.comments = self.dbclient["comments"]
        self.likes = self.dbclient["likes"]
        super().__init__()

    # =========== user data manipulation ===========
    # return the user info with specified user id
    def find_user_by_id(self, user_id):
        found_user = self.users.find_one({"_id": ObjectId(user_id)})
        if found_user:
            found_user["_id"] = str(found_user["_id"])
        return found_user

    # return the user info with specified user id
    def find_user_by_email(self, email):
        found_user = self.users.find_one({"email": email})
        if found_user:
            found_user["_id"] = str(found_user["_id"])
        return found_user

    # return all user accounts (can only be used in debug)
    def find_all_users(self):
        cursor = self.users.find()
        all_users = []
        for user in cursor:
            user["_id"] = str(user["_id"])
            all_users.append(user)
        return all_users

    # add an new user account to database
    def add_user(self, user):
        _id = str(self.users.insert_one(user).inserted_id)
        return _id

    # update the user account
    def update_user(self, user_id, update_info):
        query = {"_id": ObjectId(user_id)}
        return self.users.update_one(query, {"$set": update_info})

    # delete the user account
    def delete_user(self, user_id):
        # delte user's projects and related comments & likes
        cursor = self.projects.find({"user": user_id})
        for project in cursor:
            self.delete_project(str(project["_id"]))
        
        # delete likes
        self.likes.delete_many({"user": user_id})
        # delete comments
        self.comments.delete_many({"user": user_id})
        # delete files
        self.files.delete_many({"user": user_id})
        
        self.users.delete_one({"_id": ObjectId(user_id)})

    # =========== project data manipulation ===========
    # return the project with specified project id
    def find_project_by_id(self, project_id):
        found_project = self.projects.find_one({"_id": ObjectId(project_id)})
        if found_project:
            # change the ObjectId to string format
            found_project["_id"] = str(found_project["_id"])
        return found_project

    # return all projects
    # if a major is specified, will only return projects in that major
    def find_all_projects(self, major=""):
        all_projects = []
        if major:
            unjson_projects = self.projects.find({"major": major})
            for project in unjson_projects:
                project["_id"] = str(project["_id"])
                all_projects.append(project)
        else:
            for project in self.projects.find():
                project["_id"] = str(project["_id"])
                all_projects.append(project)
        return all_projects

    # find all projects owned by the user
    def find_user_projects(self, user_id):
        cursor = self.projects.find({"user": user_id})
        user_projects = []
        for project in cursor:
            project["_id"] = str(project["_id"])
            user_projects.append(project)
        return user_projects

    # add project to database
    def add_project(self, project):
        _id = str(self.projects.insert_one(project).inserted_id)
        return _id
    
    # update the project
    def update_project(self, project_id, update_info):
        query = {"_id": ObjectId(project_id)}
        return self.projects.update_one(query, {"$set": update_info})

    # delete the project
    def delete_project(self, project_id):
        # delete comments
        project_files = self.files.find({"project": project_id})
        for file in project_files:
            file["_id"] = str(file["_id"])
            file_comments = self.comments.find({"file": file["_id"]})
            for comment in file_comments:
                self.likes.delete_many({"comment": str(comment["_id"])})
            self.comments.delete_many({"file": file["_id"]})
        # delete files
        self.files.delete_many({"project": project_id})
        # delete projects
        self.projects.delete_one({"_id": ObjectId(project_id)})

    # =========== file data manipulation ===========
    # add file to database
    def add_file(self, file):
        self.files.insert_one(file)
    
    # return all files of the project
    def find_project_files(self, project_id):
        cursor = self.files.find({"project": project_id})
        project_files = []
        for file in cursor:
            file["_id"] = str(file["_id"])
            project_files.append(file)
        return project_files
    
    # return the file with specified file id
    def find_file_by_id(self, file_id):
        found_file = self.files.find_one({"_id": ObjectId(file_id)})
        if found_file:
            # change the ObjectId to string format
            found_file["_id"] = str(found_file["_id"])
        return found_file

    # =========== comments data manipulation ===========
    # add comment to database
    def add_comment(self, comment):
        self.comments.insert_one(comment)
        found_user = self.users.find_one({"_id": ObjectId(comment["user"])})
        # update user commentNum & points
        print(comment["user"])
        query = {"_id": ObjectId(comment["user"])}
        self.users.update_one(query, {"$set": {"commentNum": found_user["commentNum"] + 1, "points": found_user["points"] + 2}})
        
        # update file rating
        found_file = self.files.find_one({"_id": ObjectId(comment["file"])})
        file_total_rating = found_file["rating"] * found_file["ratingNum"]

        new_rating_num = found_file["ratingNum"] + 1
        new_rating = round((file_total_rating + comment["rating"]) / (new_rating_num), 2)
        query = {"_id": ObjectId(comment["file"])}
        return self.files.update_one(query, {"$set": {"ratingNum": new_rating_num, "rating": new_rating}})
        
    # return the comment with specified comment id
    def find_comment_by_id(self, comment_id):
        found_comment = self.files.find_one({"_id": ObjectId(comment_id)})
        if found_comment:
            # change the ObjectId to string format
            found_comment["_id"] = str(found_comment["_id"])
        return found_comment
    
    # return all comments of the file
    def find_file_comments(self, file_id):
        cursor = self.comments.find({"file": file_id})
        file_comments = []
        for comment in cursor:
            comment["_id"] = str(comment["_id"])
            file_comments.append(comment)
        return file_comments
            
    # =========== like data manipulation ===========
    def add_like(self, user_id, comment_id):
        like_data = {"user": user_id, "comment": comment_id}
        self.likes.insert_one(like_data)

        # update comment likedNum
        found_comment = self.comments.find_one({"_id": ObjectId(comment_id)})
        query = {"_id": ObjectId(comment_id)}
        self.comments.update_one(query, {"$set": {"likedNum": found_comment["likedNum"] + 1}})

        # update user likedNum & points
        comment_provider = self.comments.find_one({"_id": ObjectId(comment_id)})["user"]
        found_user = self.users.find_one({"_id": ObjectId(comment_provider)})
        query = {"_id": ObjectId(comment_provider)}
        self.users.update_one(query, {"$set": {"likedNum": found_user["likedNum"] + 1, "points": found_user["points"] + 1}})
    
    # check if user has liked the comment
    def user_has_liked_comment(self, user_id, comment_id):
        found_like = self.likes.find_one({"user": user_id, "comment": comment_id})
        if found_like:
            return True
        else:
            return False