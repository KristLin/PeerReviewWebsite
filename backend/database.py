from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pyodbc
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SECRET_KEY'] = '9011ee99-7669-4da4-9d71-18e3ea930e6f'
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc://Tony:Miteli34548121@@tony9323.database.windows.net:1433/Tony-9323?driver=SQL+Server"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['Format_Parse_DateTime'] = "%Y-%m-%d %H:%M:%S"
app.config['Point_Cost_for_Top'] = 10  # redeem 10 points for 1 top chance
app.config['Point_Gain_for_Comment'] = 2  # gain 2 point for every successful comment
app.config['Point_Gain_for_being_liked'] = 1  # gain 1 point for comments being liked by others

db_sqlalchemy = SQLAlchemy(app)

@app.shell_context_processor
def make_shell_context():
    return dict(db_1=db_sqlalchemy, User=User, Project=Project, File=File, Comment=Comment, Like=Like, DB=DB, db_o=DB())


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()


class User(db_sqlalchemy.Model):
    __tablename__ = 'User'
    id = db_sqlalchemy.Column(db_sqlalchemy.Integer, primary_key=True) # User ID
    name = db_sqlalchemy.Column(db_sqlalchemy.Unicode(255))  # User name
    email = db_sqlalchemy.Column(db_sqlalchemy.Unicode(255))  # User email
    registeredTime = db_sqlalchemy.Column(db_sqlalchemy.DateTime)  # User registration date and time, in SQL Alchemy 'DateTime' type
    commentTimes = db_sqlalchemy.Column(db_sqlalchemy.Integer)  # The number of comments the user made to others
    likedTimes = db_sqlalchemy.Column(db_sqlalchemy.Integer)  # The number of likes the user received from others
    topTimes = db_sqlalchemy.Column(db_sqlalchemy.Integer)  # Remaining top times the user can use
    points = db_sqlalchemy.Column(db_sqlalchemy.BigInteger)  # Points the user has, in 'BigInteger' type
    major = db_sqlalchemy.Column(db_sqlalchemy.Unicode(255))  # User major, in "IT", "Medicine", "Science" and "Business"
    password_hash = db_sqlalchemy.Column(db_sqlalchemy.Unicode(255))  # Password hash of user's password

    projects = db_sqlalchemy.relationship('Project', backref='user')
    files = db_sqlalchemy.relationship('File', backref='user')
    comments = db_sqlalchemy.relationship('Comment', backref='user')
    likes = db_sqlalchemy.relationship('Like', backref='user')

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.name

    def __init__(self, user_dict):
        if user_dict.get('name') is not None:
            self.name = user_dict.get('name')

        if user_dict.get('email') is not None:
            self.email = user_dict.get('email')

        if user_dict.get('registeredTime') is not None:
            self.registeredTime = datetime.strptime(user_dict.get('registeredTime'), app.config['Format_Parse_DateTime'])
        else:
            self.registeredTime = datetime.now()

        if user_dict.get('commentTimes') is not None:
            self.commentTimes = user_dict.get('commentTimes')
        else:
            self.commentTimes = 0

        if user_dict.get('likedTimes') is not None:
            self.likedTimes = user_dict.get('likedTimes')
        else:
            self.likedTimes = 0

        if user_dict.get('topTimes') is not None:
            self.topTimes = user_dict.get('topTimes')
        else:
            self.topTimes = 2  # New user is given 2 chances to top his/her projects

        if user_dict.get('points') is not None:
            self.points = user_dict.get('points')
        else:
            self.points = 0

        if user_dict.get('major') is not None:
            self.major = user_dict.get('major')

        if user_dict.get('password') is not None:
            self.password_hash = generate_password_hash(user_dict.get('password'))

        return

    def set_from_dict(self, user_dict):
        if user_dict.get('name') is not None:
            self.name = user_dict.get('name')
        if user_dict.get('email') is not None:
            self.email = user_dict.get('email')
        if user_dict.get('registeredTime') is not None:
            self.registeredTime = datetime.strptime(user_dict.get('registeredTime'),  app.config['Format_Parse_DateTime'])
        if user_dict.get('commentTimes') is not None:
            self.commentTimes = user_dict.get('commentTimes')

        if user_dict.get('likedTimes') is not None:
            self.likedTimes = user_dict.get('likedTimes')
        if user_dict.get('topTimes') is not None:
            self.topTimes = user_dict.get('topTimes')
        if user_dict.get('points') is not None:
            self.points = user_dict.get('points')
        if user_dict.get('major') is not None:
            self.major = user_dict.get('major')
        if user_dict.get('password') is not None:
            self.password_hash = generate_password_hash(user_dict.get('password'))

        return

    def get_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'registeredTime': self.registeredTime,
            'commentTimes': self.commentTimes,
            'likedTimes': self.likedTimes,
            'topTimes': self.topTimes,
            'points': self.points,
            'major': self.major
        }


class Project(db_sqlalchemy.Model):
    __tablename__ = 'Project'
    id = db_sqlalchemy.Column(db_sqlalchemy.Integer, primary_key=True) # Project ID
    createdByUser = db_sqlalchemy.Column(db_sqlalchemy.Integer, db_sqlalchemy.ForeignKey('User.id'))  # [Foreign key] Created by which user
    createdTime = db_sqlalchemy.Column(db_sqlalchemy.DateTime)  # Created Date and Time, also used for top ordering, in SQL Alchemy 'DateTime' type
    projectName = db_sqlalchemy.Column(db_sqlalchemy.Unicode(255))  # Project name
    description = db_sqlalchemy.Column(db_sqlalchemy.UnicodeText) # Project description, in SQL Alchemy 'Text' type
    isOnTop = db_sqlalchemy.Column(db_sqlalchemy.Boolean, default=False) # Is this project topped?

    files = db_sqlalchemy.relationship('File', backref='project')

    def __repr__(self):
        return '<Project %r>' % self.projectName

    def __init__(self, project_dict):
        if project_dict.get('createdByUser') is not None:
            self.createdByUser = project_dict.get('createdByUser')

        if project_dict.get('createdTime') is not None:
            self.createdTime = datetime.strptime(project_dict.get('createdTime'), app.config['Format_Parse_DateTime'])
        else:
            self.createdTime = datetime.now()

        if project_dict.get('projectName') is not None:
            self.projectName = project_dict.get('projectName')
        else:
            self.projectName = "Unnamed Project"

        if project_dict.get('description') is not None:
            self.description = project_dict.get('description')

        if project_dict.get('isOnTop') not in [None, 'False', 'false', 'F', 'f', 'No', 'no', 'N', 'n', '0', 0]:
            self.isOnTop = True
        else:
            self.isOnTop = False  # By default a new project is not on top

        return

    def set_from_dict(self, project_dict):
        if project_dict.get('createdByUser') is not None:
            self.createdByUser = project_dict.get('createdByUser')

        if project_dict.get('createdTime') is not None:
            self.createdTime = datetime.strptime(project_dict.get('createdTime'), app.config['Format_Parse_DateTime'])

        if project_dict.get('projectName') is not None:
            self.projectName = project_dict.get('projectName')

        if project_dict.get('description') is not None:
            self.description = project_dict.get('description')

        if project_dict.get('isOnTop') is not None:
            if project_dict.get('isOnTop') not in [None, 'False', 'false', 'F', 'f', 'No', 'no', 'N', 'n', '0', 0]:
                self.isOnTop = True
            else:
                self.isOnTop = False

        return

    def get_dict(self):
        return {
            'id': self.id,
            'createdByUser': self.createdByUser,
            'createdTime': self.createdTime,
            'projectName': self.projectName,
            'description': self.description,
            'isOnTop': self.isOnTop
        }


class File(db_sqlalchemy.Model):
    __tablename__ = 'File'
    id = db_sqlalchemy.Column(db_sqlalchemy.Integer, primary_key=True)  # File ID
    inProject = db_sqlalchemy.Column(db_sqlalchemy.Integer, db_sqlalchemy.ForeignKey('Project.id'))  # [Foreign key] In which project stays the file
    uploadByUser = db_sqlalchemy.Column(db_sqlalchemy.Integer, db_sqlalchemy.ForeignKey('User.id'))  # [Foreign key] Uploaded by which user
    uploadTime = db_sqlalchemy.Column(
        db_sqlalchemy.DateTime)  # Upload Date and Time, in SQL Alchemy 'DateTime' type
    fileName = db_sqlalchemy.Column(db_sqlalchemy.Unicode(255))  # File name
    fileContent = db_sqlalchemy.Column(db_sqlalchemy.UnicodeText)  # File content, in SQL Alchemy 'Text' type
    averageRating = db_sqlalchemy.Column(db_sqlalchemy.Float)  # Average rating on this file

    comments = db_sqlalchemy.relationship('Comment', backref='file')

    def __repr__(self):
        return '<File %r>' % self.fileName

    def __init__(self, file_dict):
        if file_dict.get('inProject') is not None:
            self.inProject = file_dict.get('inProject')

        if file_dict.get('uploadByUser') is not None:
            self.uploadByUser = file_dict.get('uploadByUser')

        if file_dict.get('uploadTime') is not None:
            self.uploadTime = datetime.strptime(file_dict.get('uploadTime'), app.config['Format_Parse_DateTime'])
        else:
            self.uploadTime = datetime.now()

        if file_dict.get('fileName') is not None:
            self.fileName = file_dict.get('fileName')
        else:
            self.fileName = "Unnamed File"

        if file_dict.get('fileContent') is not None:
            self.fileContent = file_dict.get('fileContent')

        if file_dict.get('averageRating') is not None:
            self.averageRating = file_dict.get('averageRating')
        else:
            self.averageRating = 0

        return

    def set_from_dict(self, file_dict):
        if file_dict.get('inProject') is not None:
            self.inProject = file_dict.get('inProject')

        if file_dict.get('uploadByUser') is not None:
            self.uploadByUser = file_dict.get('uploadByUser')

        if file_dict.get('uploadTime') is not None:
            self.uploadTime = datetime.strptime(file_dict.get('uploadTime'), app.config['Format_Parse_DateTime'])

        if file_dict.get('fileName') is not None:
            self.fileName = file_dict.get('fileName')

        if file_dict.get('fileContent') is not None:
            self.fileContent = file_dict.get('fileContent')

        if file_dict.get('averageRating') is not None:
            self.averageRating = file_dict.get('averageRating')

        return

    def get_dict(self):
        return {
            'id': self.id,
            'inProject': self.inProject,
            'uploadByUser': self.uploadByUser,
            'uploadTime': self.uploadTime,
            'fileName': self.fileName,
            'fileContent': self.fileContent,
            'averageRating': self.averageRating
        }


class Comment(db_sqlalchemy.Model):
    __tablename__ = 'Comment'
    id = db_sqlalchemy.Column(db_sqlalchemy.Integer, primary_key=True)  # Comment ID
    onFile = db_sqlalchemy.Column(db_sqlalchemy.Integer, db_sqlalchemy.ForeignKey('File.id'))  # [Foreign key] on which file stays the comment
    postByUser = db_sqlalchemy.Column(db_sqlalchemy.Integer, db_sqlalchemy.ForeignKey('User.id'))  # [Foreign key] Comment posted by which user
    postTime = db_sqlalchemy.Column(
        db_sqlalchemy.DateTime)  # Comment post Date and Time, in SQL Alchemy 'DateTime' type
    commentContent = db_sqlalchemy.Column(db_sqlalchemy.UnicodeText)  # Comment content, in SQL Alchemy 'Text' type
    ratingForFile = db_sqlalchemy.Column(db_sqlalchemy.Integer)  # Rating (from 1 to 5) for the file

    likes = db_sqlalchemy.relationship('Like', backref='comment')

    def __repr__(self):
        return '<Comment %r>' % self.id

    def __init__(self, comment_dict):
        if comment_dict.get('onFile') is not None:
            self.onFile = comment_dict.get('onFile')

        if comment_dict.get('postByUser') is not None:
            self.postByUser = comment_dict.get('postByUser')

        if comment_dict.get('postTime') is not None:
            self.postTime = datetime.strptime(comment_dict.get('postTime'), app.config['Format_Parse_DateTime'])
        else:
            self.postTime = datetime.now()

        if comment_dict.get('commentContent') is not None:
            self.commentContent = comment_dict.get('commentContent')

        if comment_dict.get('ratingForFile') is not None:
            self.ratingForFile = comment_dict.get('ratingForFile')

        return

    def set_from_dict(self, comment_dict):
        if comment_dict.get('onFile') is not None:
            self.onFile = comment_dict.get('onFile')

        if comment_dict.get('postByUser') is not None:
            self.postByUser = comment_dict.get('postByUser')

        if comment_dict.get('postTime') is not None:
            self.postTime = datetime.strptime(comment_dict.get('postTime'), app.config['Format_Parse_DateTime'])

        if comment_dict.get('commentContent') is not None:
            self.commentContent = comment_dict.get('commentContent')

        if comment_dict.get('ratingForFile') is not None:
            self.ratingForFile = comment_dict.get('ratingForFile')

        return

    def get_dict(self):
        return {
            'id': self.id,
            'onFile': self.onFile,
            'postByUser': self.postByUser,
            'postTime': self.postTime,
            'commentContent': self.commentContent,
            'ratingForFile': self.ratingForFile
        }


class Like(db_sqlalchemy.Model):
    __tablename__ = 'Like'
    id = db_sqlalchemy.Column(db_sqlalchemy.Integer, primary_key=True)  # Like ID
    onComment = db_sqlalchemy.Column(db_sqlalchemy.Integer, db_sqlalchemy.ForeignKey('Comment.id'))  # [Foreign key] for which comment stays the like
    likedByUser = db_sqlalchemy.Column(db_sqlalchemy.Integer, db_sqlalchemy.ForeignKey('User.id'))  # [Foreign key] Like given by which user
    likedTime = db_sqlalchemy.Column(
        db_sqlalchemy.DateTime)  # Like submission Date and Time, in SQL Alchemy 'DateTime' type

    def __repr__(self):
        return '<Like %r>' % self.id

    def __init__(self, like_dict):
        if like_dict.get('onComment') is not None:
            self.onComment = like_dict.get('onComment')

        if like_dict.get('likedByUser') is not None:
            self.likedByUser = like_dict.get('likedByUser')

        if like_dict.get('likedTime') is not None:
            self.likedTime = datetime.strptime(like_dict.get('likedTime'), app.config['Format_Parse_DateTime'])
        else:
            self.likedTime = datetime.now()

        return

    def set_from_dict(self, like_dict):
        if like_dict.get('onComment') is not None:
            self.onComment = like_dict.get('onComment')

        if like_dict.get('likedByUser') is not None:
            self.likedByUser = like_dict.get('likedByUser')

        if like_dict.get('likedTime') is not None:
            self.likedTime = datetime.strptime(like_dict.get('likedTime'), app.config['Format_Parse_DateTime'])

        return

    def get_dict(self):
        return {
            'id': self.id,
            'onComment': self.onComment,
            'likedByUser': self.likedByUser,
            'likedTime': self.likedTime
        }


# class DB(db_sqlalchemy):
class DB(object):
    def __init__(self):
        super().__init__()

    # =========== user data manipulation ===========
    @staticmethod
    def find_user_by_id(user_id):
        m_user = User.query.get(user_id)
        if m_user is None:
            return None  # return None if no User record returned from Database and no User object generated.
        else:
            return m_user.get_dict()

    @staticmethod
    def find_user_by_email(email):
        m_user = User.query.filter_by(email=email).first()  # return None or just one user objects
        if len(m_user) is 0:
            return None
        else:
            return m_user.get_dict()

    @staticmethod
    def find_all_users():
        m_users = User.query.all()  # return None or a list of User objects
        if len(m_users) is 0:
            return None
        else:
            user_list = []
            for m_single_user in m_users:
                user_list.append(m_single_user.get_dict())
            return user_list

    @staticmethod
    def add_user(user):
        m_user = User(user)
        if not m_user:
            return False

        db_sqlalchemy.session.add(m_user)
        try:
            db_sqlalchemy.session.commit()
            return True
        except:
            db_sqlalchemy.session.rollback()
            raise
        finally:
            db_sqlalchemy.session.close()

    # update & delete need to return a flag
    @staticmethod
    def update_user(user):
        m_id = user.get('id')
        if m_id is None:
            return False

        m_user = User.query.get(m_id)
        if m_user is None:
            return False

        m_user.set_from_dict(user)

        db_sqlalchemy.session.add(m_user)
        try:
            db_sqlalchemy.session.commit()
            return True
        except:
            db_sqlalchemy.session.rollback()
            raise
        finally:
            db_sqlalchemy.session.close()

    @staticmethod
    def delete_user(user_id):
        m_user = User.query.get(user_id)
        if m_user is None:
            return False
        else:
            db_sqlalchemy.session.delete(m_user)
            try:
                db_sqlalchemy.session.commit()
                return True
            except:
                db_sqlalchemy.session.rollback()
                raise
            finally:
                db_sqlalchemy.session.close()




    # =========== project data manipulation ===========
    @staticmethod
    def find_project_by_id(project_id):
        m_project = Project.query.get(project_id)
        if m_project is None:
            return None  # return None if no project record returned from Database and no project object generated.
        else:
            return m_project.get_dict()

    @staticmethod
    def find_all_projects():
        m_projects = Project.query.order_by(Project.isOnTop.desc(), Project.createdTime.desc()).all()  # return None or a list of project objects
        if len(m_projects) is 0:
            return None
        else:
            project_list = []
            for m_single_project in m_projects:
                project_list.append(m_single_project.get_dict())
            return project_list
        # Topped projects are made on top of the list
        # In topped and untopped group, all projects are sorted on descending order by its 'createdTime'

    @staticmethod
    def find_all_projects_of_a_user(user_id):
        m_projects = Project.query.filter_by(createdByUser=user_id).order_by(Project.isOnTop.desc(), Project.createdTime.desc()).all()
        if len(m_projects) is 0:
            return None
        else:
            project_list = []
            for m_single_project in m_projects:
                project_list.append(m_single_project.get_dict())
            return project_list
        # Topped projects are made on top of the list
        # In topped and untopped group, all projects are sorted on descending order by its 'createdTime'

    @staticmethod
    def add_project(project):
        m_project = Project(project)
        if not m_project:
            return False

        db_sqlalchemy.session.add(m_project)
        try:
            db_sqlalchemy.session.commit()
            return True
        except:
            db_sqlalchemy.session.rollback()
            raise
        finally:
            db_sqlalchemy.session.close()

    @staticmethod
    def update_project(project):
        m_id = project.get('id')
        if m_id is None:
            return False

        m_project = Project.query.get(m_id)
        if m_project is None:
            return False

        m_project.set_from_dict(project)

        db_sqlalchemy.session.add(m_project)
        try:
            db_sqlalchemy.session.commit()
            return True
        except:
            db_sqlalchemy.session.rollback()
            raise
        finally:
            db_sqlalchemy.session.close()

    @staticmethod
    def make_project_on_top(project_id):  # Make a project on top of others, and refresh the createdTime as now

        m_project = Project.query.get(project_id)
        if m_project is None:
            return None  # return None if no project record returned from Database

        if m_project.isOnTop is True:
            return False  # return False if the project is already on top

        if m_project.user is None:
            return False  # return False if the creator of the project is unknown

        if m_project.user.topTimes < 1:
            return False  # return False if the user doesn't have enough top chances

        m_project.isOnTop = True
        m_project.createdTime = datetime.now()
        m_project.user.topTimes -= 1

        db_sqlalchemy.session.add(m_project)
        #db_sqlalchemy.session.add(m_project.user)  # No need to add modified user record to session separately
        try:
            db_sqlalchemy.session.commit()
            return True
        except:
            db_sqlalchemy.session.rollback()
            raise
        finally:
            db_sqlalchemy.session.close()



    # =========== file data manipulation ===========
    @staticmethod
    def find_file_by_id(file_id):
        m_file = File.query.get(file_id)
        if m_file is None:
            return None  # return None if no file record returned from Database and no file object generated.
        else:
            return m_file.get_dict()

    @staticmethod
    def find_all_files_of_a_project(project_id):
        m_files = File.query.filter_by(inProject=project_id).order_by(File.uploadTime.desc()).all()
        if len(m_files) == 0:
            return None
        else:
            file_list = []
            for m_single_file in m_files:
                file_list.append(m_single_file.get_dict())
            return file_list

    @staticmethod
    def find_all_files_of_a_user(user_id):
        m_files = File.query.filter_by(uploadByUser=user_id).order_by(File.uploadTime.desc()).all()
        if len(m_files) == 0:
            return None
        else:
            file_list = []
            for m_single_file in m_files:
                file_list.append(m_single_file.get_dict())
            return file_list

    @staticmethod
    def add_file(file):
        m_file = File(file)
        if not m_file:
            return False

        db_sqlalchemy.session.add(m_file)
        try:
            db_sqlalchemy.session.commit()
            return True
        except:
            db_sqlalchemy.session.rollback()
            raise
        finally:
            db_sqlalchemy.session.close()

    @staticmethod
    def update_file(file):
        m_id = file.get('id')
        if m_id is None:
            return False

        m_file = File.query.get(m_id)
        if m_file is None:
            return False

        m_file.set_from_dict(file)

        db_sqlalchemy.session.add(m_file)
        try:
            db_sqlalchemy.session.commit()
            return True
        except:
            db_sqlalchemy.session.rollback()
            raise
        finally:
            db_sqlalchemy.session.close()




# =========== comment data manipulation ===========
    @staticmethod
    def find_comment_by_id(comment_id):
        m_comment = Comment.query.get(comment_id)
        if m_comment is None:
            return None  # return None if no comment record returned from Database and no comment object generated.
        else:
            return m_comment.get_dict()

    @staticmethod
    def find_all_comments_on_a_file(file_id):
        m_comments = Comment.query.filter_by(onFile=file_id).order_by(Comment.postTime.desc()).all()
        if len(m_comments) == 0:
            return None
        else:
            comment_list = []
            for m_single_comment in m_comments:
                comment_list.append(m_single_comment.get_dict())
            return comment_list

    @staticmethod
    def find_all_comments_of_a_user(user_id):
        m_comments = Comment.query.filter_by(postByUser=user_id).order_by(Comment.postTime.desc()).all()
        if len(m_comments) == 0:
            return None
        else:
            comment_list = []
            for m_single_comment in m_comments:
                comment_list.append(m_single_comment.get_dict())
            return comment_list

    @staticmethod
    def post_comment(comment):
        user_id = comment.get('postByUser')
        if user_id is None:  # Anonymous comments are not allowed
            return False

        file_id = comment.get('onFile')
        if file_id is None:  # A comment must be related to a file
            return False

        m_comment = Comment(comment)
        if not m_comment:
            return False

        m_user = User.query.get(user_id)
        if m_user is None:
            return False

        m_file = File.query.get(file_id)
        if m_file is None:
            return False

        #m_comment.user.commentTimes += 1
        #m_comment.user.points += app.config['Point_Gain_for_Comment']
        m_user.commentTimes += 1
        m_user.points += app.config['Point_Gain_for_Comment']

        if comment.get('ratingForFile') is not None:
            if m_file.averageRating is None or m_file.averageRating == 0:
                m_file.averageRating = comment.get('ratingForFile')
            else:
                m_file.averageRating = 0.95 * m_file.averageRating + 0.05 * comment.get('ratingForFile')

        db_sqlalchemy.session.add(m_file)
        db_sqlalchemy.session.add(m_comment)
        db_sqlalchemy.session.add(m_user)
        try:
            db_sqlalchemy.session.commit()
            return True
        except:
            db_sqlalchemy.session.rollback()
            raise
        finally:
            db_sqlalchemy.session.close()

    @staticmethod
    def update_comment(comment):
        m_id = comment.get('id')
        if m_id is None:
            return False

        m_comment = Comment.query.get(m_id)
        if m_comment is None:
            return False

        m_comment.set_from_dict(comment)

        db_sqlalchemy.session.add(m_comment)
        try:
            db_sqlalchemy.session.commit()
            return True
        except:
            db_sqlalchemy.session.rollback()
            raise
        finally:
            db_sqlalchemy.session.close()

    @staticmethod
    def comment_count_by_file(file_id):
        m_count = Comment.query.filter_by(onFile=file_id).count()
        return {
            'fileId': file_id,
            'commentCount': m_count
        }

    @staticmethod
    def comment_count_by_user(user_id):
        m_count = Comment.query.filter_by(postByUser=user_id).count()
        return {
            'userId': user_id,
            'commentCount': m_count
        }


# =========== likes data manipulation ===========
    @staticmethod
    def find_like_by_id(like_id):
        m_like = Comment.query.get(like_id)
        if m_like is None:
            return None  # return None if no like record returned from Database and no like object generated.
        else:
            return m_like.get_dict()

    @staticmethod
    def find_all_like_on_a_comment(comment_id):
        m_likes = Like.query.filter_by(onComment=comment_id).order_by(Like.likedTime.desc()).all()
        if len(m_likes) == 0:
            return None
        else:
            like_list = []
            for m_single_like in m_likes:
                like_list.append(m_single_like.get_dict())
            return like_list

    @staticmethod
    def find_all_likes_of_a_user(user_id):
        m_likes = Like.query.filter_by(likedByUser=user_id).order_by(Like.likedTime.desc()).all()
        if len(m_likes) == 0:
            return None
        else:
            like_list = []
            for m_single_like in m_likes:
                like_list.append(m_single_like.get_dict())
            return like_list

    @staticmethod
    def is_user_liked_this_comment(user_id, comment_id):
        if Like.query.filter_by(likedByUser=user_id, onComment=comment_id).count() is not 0:
            return True  # user already liked this comment
        else:
            return False  # user hasn't liked this comment

    @staticmethod
    def give_a_like(like):

        user_id = like.get('likedByUser')
        if user_id is None:  # Anonymous likes are not allowed
            return False

        comment_id = like.get('onComment')
        if comment_id is None:  # A like must be related to a comment
            return False

        if DB.is_user_liked_this_comment(user_id, comment_id):
            return False  # User already liked this comment

        m_like = Like(like)
        if not m_like:
            return False

        m_comment = Comment.query.get(comment_id)   # to open the being-liked user object to credit him/her with points
        if comment_id is None:
            return False

        m_comment.user.likedTimes += 1
        m_comment.user.points += app.config['Point_Gain_for_being_liked']

        db_sqlalchemy.session.add(m_like)
        db_sqlalchemy.session.add(m_comment)
        try:
            db_sqlalchemy.session.commit()
            return True
        except:
            db_sqlalchemy.session.rollback()
            raise
        finally:
            db_sqlalchemy.session.close()

    @staticmethod
    def cancel_a_like(like):
        user_id = like.get('likedByUser')
        if user_id is None:  # Anonymous likes are not allowed
            return False

        comment_id = like.get('onComment')
        if comment_id is None:  # A like must be related to a comment
            return False

        if not DB.is_user_liked_this_comment(user_id, comment_id):
            return False

        m_like = Like.query.filter_by(likedByUser=user_id, onComment=comment_id).first()
        db_sqlalchemy.session.delete(m_like)
        try:
            db_sqlalchemy.session.commit()
            return True
        except:
            db_sqlalchemy.session.rollback()
            raise
        finally:
            db_sqlalchemy.session.close()


    @staticmethod
    def like_count_by_comment(comment_id):
        m_count = Like.query.filter_by(onComment=comment_id).count()
        return {
            'comment_id': comment_id,
            'likeCount': m_count
        }

    @staticmethod
    def like_count_by_user(user_id):
        m_count = Like.query.filter_by(likedByUser=user_id).count()
        return {
            'userId': user_id,
            'likeCount': m_count
        }