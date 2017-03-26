import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True) #this allow you to search easily
    username = db.Column(db.String(80)) #the 80 refers to the limit of the columns
    password = db.Column(db.String(80)) #creates another column

    def __init__(self, username, password): #you don't need '_id' as it is a primary key
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first() #the latter username refers to the method's argument, the first one is a filter #this returns SELECT * FROM users

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
#This is an API, because it allows other parts of the program to interact with the user
