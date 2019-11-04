from flask import Flask, request
from flask_restplus import Resource, Api, fields
from flask_cors import CORS
import requests
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash

import os
from datetime import datetime

from database import DB
import utils

app = Flask(__name__)

CORS(app)
db = DB()

# store active users
active_users = {}

api = Api(
    app,
    version="1.0",
    #  Documentation Title
    title="Peer Review Database",
    #  Documentation Description
    description="Peer Review backend APIs.",
)

# set namespaces, remvoe the default namespace before adding new
api.namespaces.clear()
users = api.namespace("users", description="User APIs")
projects = api.namespace("projects", description="Project APIs")
files = api.namespace("files", description="File APIs")
test = api.namespace("test", description="Test APIs")
# =============== app setting part end ===============

# =============== data model part start ===============
# user data model
user_model = api.model(
    "user",
    {
        "email": fields.String(
            # required=True,
            description="Email of the user",
            help="Email cannot be blank.",
        ),
        "name": fields.String,
        "password": fields.String,
        "major": fields.String,
        # following data will be set automatically before added
        "registeredTime": fields.String,
        "commentTimes": fields.String,
        "likedTimes": fields.String,
        "topTimes": fields.String,
        "points": fields.String,
    },
)

# login data model
login_model = api.model(
    "login",
    {
        "email": fields.String(
            # required=True,
            description="Email of the user",
            help="Email cannot be blank.",
        ),
        "password": fields.String,
    },
)

# project data model
project_model = api.model(
    "project",
    {
        "createdByUser": fields.String,
        "major": fields.String,
        "projectName": fields.String,
        "description": fields.String,
        "createdTime": fields.String,
        "isOnTop": fields.Boolean,
    },
)

# file data model
file_model = api.model(
    "file",
    {
        "inProject": fields.String,
        "uploadByUser": fields.String,
        "fileName": fields.String,
        "fileContent": fields.String,
        "uploadTime": fields.String,
        "averageRating": fields.String
    },
)

# comment data model
comment_model = api.model(
    "comment",
    {
        "onFile": fields.String,
        "postByUser": fields.String,
        "commentContent": fields.String,
        "postTime": fields.String,
        "ratingForFile": fields.Integer,
    },
)

# =============== data model part end ===============

# ============ user API part start ============
@users.route("/")
class UsersAPI(Resource):
    @api.doc(description="Register a new user account")
    @api.expect(user_model, validate=True)
    def post(self):
        user_data = request.json
        if db.find_user_by_email(user_data["email"]):
            return "The email already exists.", 400
        else:
            if db.add_user(user_data):
                user_data = db.find_user_by_email(user_data["email"])
                active_users[user_data["email"]] = user_data
                return user_data["id"] + " " + user_data["major"] + " " + user_data["name"], 200
            else:
                return "Error", 400

    @api.doc(description="get all users (only used for test)")
    def get(self):
        all_users = db.find_all_users()
        return all_users, 200


@users.route("/login")
class LoginAPI(Resource):
    @api.doc(description="Log in an user account")
    @api.expect(login_model, validate=True)
    def post(self):
        user_login_data = request.json

        if user_login_data["email"] in active_users:
            user_data = active_users[user_login_data["email"]]
            print(user_data["email"] + " has Already logged in")
            return user_data["id"] + " " + user_data["major"] + " " + user_data["name"], 200
        
        login_user = db.find_user_by_email(user_login_data["email"])
        if login_user == None:
            return "The user email does not exist", 400
        
        if check_password_hash(login_user["password"], user_login_data["password"]):
            # store active user info
            active_users[login_user["email"]] = login_user
            return login_user["id"] + " " + login_user["major"] + " " + login_user["name"], 200
        else:
            return "Password is wrong", 400


@users.route("/logout/<string:user_id>")
class LogoutAPI(Resource):
    @api.doc(description="Log out an user account")
    def get(self, user_id):
        user_data = db.find_user_by_id(user_id)
        if user_data["email"] in active_users:
            del active_users[user_data["email"]]
        else:
            print("User is not in the active list, maybe the server has restarted.")
        return "Log out successfully", 200


@users.route("/<string:user_id>")
class UserAPI(Resource):
    @api.doc(description="Return user info (except password)")
    def get(self, user_id):
        userData = db.find_user_by_id(user_id)
        if userData:
            del userData["password"]
            return userData, 200
        else:
            return f"User with id {user_id} is not in the database!", 400

    # @api.doc(description="Delete a user by its ID")
    # def delete(self, user_id):
    #     delete_user = db.find_user_by_id(user_id)
    #     if delete_user:
    #         if user_id == delete_user["_id"]:
    #             db.delete_houses_of_user(user_id)
    #             db.delete_user(user_id)
    #             if user_id in active_users:
    #                 del active_users[user_id]
    #             msg = {"message": f"User = {user_id} is removed from the database!"}
    #             return msg, 200
    #         else:
    #             return "Unauthorized delete request", 401
    #     else:
    #         return f"User with id {user_id} is not in the database!", 400


    # @api.doc(description="Update user info")
    # def patch(self, user_id):
    #     update_info = request.json
    #     # remove empty property in update info
    #     update_info = utils.get_valid_update_info(update_info)

    #     update_user = db.find_user_by_id(user_id)
    #     if update_user:
    #         db.update_user(user_id, update_info)
    #         msg = {"message": "The user info is updated!"}
    #         return msg, 200
    #     else:
    #         return f"User with id {user_id} is not in the database!", 400
# ============ user API part end ============

# ============ project API part start ============
@projects.route("/")
class ProjectsAPI(Resource):
    @api.doc(description="Create a new project")
    @api.expect(project_model, validate=True)
    def post(self):
        project_data = request.json
        if db.add_project(project_data):
            return "Project is uploaded", 200
        else:
            return "Error", 400

    @api.doc(description="Get all projects")
    @api.param("major", "Get all projects of chosen major")
    def get(self):
        print(request.args.get("major"))
        # all_projects = db.find_all_projects(user_major)
        all_projects = db.find_all_projects()

        # attach files to project
        for project in all_projects:
            project["files"] = db.find_all_files_of_a_project(project["id"])
        return all_projects, 200

@projects.route("/<string:project_id>")
class ProjectAPI(Resource):
    @api.doc(description="Get project by its id")
    def get(self, project_id):
        project_data = db.find_project_by_id(project_id)
        if project_data:
            return project_data, 200
        else:
            return f"Project with id {project_id} is not in the database!", 400
# ============ project API part end ============

# ============ file API part start ============
@files.route("/")
class FilesAPI(Resource):
    @api.doc(description="Create a new File")
    @api.expect(file_model, validate=True)
    def post(self):
        file_data = request.json
        if db.add_file(file_data):
            return "File is uploaded", 200
        else:
            return "Error", 400

    @api.doc(description="Get all files of a project")
    @api.param("project_id", "project's id")
    def get(self):
        project_id = request.args.get("project_id")
        if project_id:
            files = db.find_all_files_of_a_project(project_id)
            return files, 200
        else:
            return "Error", 400

@files.route("/<string:file_id>")
class FileAPI(Resource):
     def get(self, file_id):
        file_data = db.find_file_by_id(file_id)
        if file_data:
            return file_data, 200
        else:
            return f"File with id {file_id} is not in the database!", 400
# ============ file API part end ============

# ============ test API part start ============
# @test.route("/")
# class TestAPI(Resource):
#     def get(self):
#         now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         data = {"num": 5, "float": 3.35, "time": now}
#         return data, 200
#     def post(self):
#         postData = request.json
#         print(postData)
#         return "OK", 200

# run the app
if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
