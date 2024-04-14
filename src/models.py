import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    username = Column(String(50),nullable=False)
    firstname = Column(String(50),nullable=False)
    lastname = Column(String(50),nullable=False)
    image_url = Column(String(150))

class Followers(Base):
    __tablename__ = "followers"
    id = Column(Integer, primary_key=True)
    followers_id = Column(Integer, ForeignKey("users.id"))
    following_id = Column(Integer, ForeignKey("users.id"))
    followers = relationship(Users)  
    following = relationship(Users)  

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship(Users)  

class Media(Base):
    __tablename__ = "media"
    id = Column(Integer, primary_key=True)
    url = Column(String(150))
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship(Post)  
    
class Comments(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(200))
    author_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("post.id"))
    author = relationship(Users)  
    post = relationship(Post) 


    def to_dict(self):
        return {}

try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
