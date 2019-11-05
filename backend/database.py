from pymongo import MongoClient
from bson import ObjectId
from random import sample

# Database to manipulate user & house data
class DB(object):
    def __init__(self):
        # connect to mongoDB mlab
        self.dbclient = MongoClient(f"mongodb://krist123:krist123@ds141188.mlab.com:41188/9323-project", 123456,).get_default_database()
        self.users = self.dbclient["users"]
        self.projects = self.dbclient["projects"]
        self.files = self.dbclient["files"]
        self.comments = self.dbclient["comments"]
        self.likes = self.dbclient["likes"]
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

    def delete_user(self, user_id):
        self.users.delete_one({"_id": ObjectId(user_id)})

    # =========== project data manipulation ===========
    def find_project_by_id(self, project_id):
        found_project = self.projects.find_one({"_id": ObjectId(project_id)})
        if found_project:
            # change the ObjectId to string format
            found_project["_id"] = str(found_project["_id"])
        return found_project

    def find_all_projects(self, major=""):
        cursor = self.projects.find()
        all_projects = []
        if major:
            for project in cursor:
                if project["major"] == major:
                    project["_id"] = str(project["_id"])
                    all_projects.append(project)
        else:
            for project in cursor:
                project["_id"] = str(project["_id"])
                all_projects.append(project)
        return all_projects

    def find_user_projects(self, user_id):
        cursor = self.projects.find()
        user_projects = []
        for project in cursor:
            if project["user"] == user_id:
                project["_id"] = str(project["_id"])
                user_projects.append(project)
        return user_projects

    def add_project(self, project):
        _id = str(self.projects.insert_one(project).inserted_id)
        return _id

    def update_project(self, project_id, update_info):
        query = {"_id": ObjectId(project_id)}
        return self.projects.update_one(query, {"$set": update_info})

    def delete_project(self, project_id):
        self.projects.delete_one({"_id": ObjectId(project_id)})
    
    def delete_projects_of_user(self, user_id):
        cursor = self.projects.find()
        user_projects = []
        for project in cursor:
            if project["user"] == user_id:
                user_projects.append(str(project["_id"]))
        for project_id in user_projects:
            self.delete_project(project_id)

    # =========== file data manipulation ===========
    def add_file(self, file):
        self.files.insert_one(file)

    def find_project_files(self, project_id):
        cursor = self.files.find()
        project_files = []
        for file in cursor:
            if file["project"] == project_id:
                file["_id"] = str(file["_id"])
                project_files.append(file)
        return project_files
    
    def find_file_by_id(self, file_id):
        found_file = self.files.find_one({"_id": ObjectId(file_id)})
        if found_file:
            # change the ObjectId to string format
            found_file["_id"] = str(found_file["_id"])
        return found_file

    def update_file_rating(self, file_id, rating):
        found_file = self.files.find_one({"_id": ObjectId(file_id)})

        file_total_rating = found_file["rating"] * found_file["ratingNum"]

        new_rating_num = found_file["ratingNum"] + 1
        new_rating = round((file_total_rating + rating) / (new_rating_num), 2)

        query = {"_id": ObjectId(file_id)}
        return self.projects.update_one(query, {"$set": {"ratingNum": new_rating_num, "rating": new_rating}})

    # =========== comments data manipulation ===========
    def add_comment(self, comment):
        self.comments.insert_one(comment)
        found_user = self.users.find_one({"_id": ObjectId(comment["user"])})
        # update user commentNum & points
        query = {"_id": ObjectId(comment["user"])}
        self.comments.update_one(query, {"$set": {"commentNum": found_user["commentNum"] + 1, "points": found_user["points"] + 2}})

    def find_comment_by_id(self, comment_id):
        found_comment = self.files.find_one({"_id": ObjectId(comment_id)})
        if found_comment:
            # change the ObjectId to string format
            found_comment["_id"] = str(found_comment["_id"])
        return found_comment

    def find_file_comments(self, file_id):
        cursor = self.comments.find()
        file_comments = []
        for comment in cursor:
            if comment["file"] == file_id:
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
        found_user = self.users.find_one({"_id": ObjectId(user_id)})
        query = {"_id": ObjectId(user_id)}
        self.comments.update_one(query, {"$set": {"likedNum": found_user["likedNum"] + 1, "points": found_user["points"] + 1}})
    
    def user_has_liked_comment(self, user_id, comment_id):
        found_like = self.likes.find_one({"user": ObjectId(user_id), "comment": comment_id})
        if found_like:
            return True
        else:
            return False