import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

#class Person(Base):
#    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
#    id = Column(Integer, primary_key=True)
#    name = Column(String(250), nullable=False)

#class Address(Base):
#    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
#    id = Column(Integer, primary_key=True)
#    street_name = Column(String(250))
#    street_number = Column(String(250))
#    post_code = Column(String(250), nullable=False)
#    person_id = Column(Integer, ForeignKey('person.id'))
#    person = relationship(Person)

#    def to_dict(self):
#        return {}

class Follower(Base):
    __tablename__ = "follower"

    id = Column(Integer, primary_key=True)
#    user_from_id = Column(Integer, primary_key=True)
    user_to_id = Column(Integer)
    user_id = Column(ForeignKey("user.id"))

class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer,primary_key=True)
    comment_text = Column(String(150))
    author_id = Column(Integer)
    post_id = (Integer)
    user_id = Column(ForeignKey("user.id"))
    post_id = Column(ForeignKey("post.id"))

class Media(Base):
    __tablename__ = "media"

    id = Column(Integer,primary_key=True)
    type_media = Column(String(10))
    url = Column(String(150))
    post_id = Column(Integer)
    post_id = Column(ForeignKey("post.id"))

class Post(Base):
    __tablename__ = "post"

    id = Column(Integer,primary_key=True)
    user_id = Column(ForeignKey("user.id"))
    comment = relationship(Comment)
    media = relationship(Media)

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    user_name = Column(String(15))
    first_name = Column(String(15))
    last_name = Column(String(15))
    email = Column(String(50))
    follower = relationship(Follower)
    post = relationship(Post)
    comment = relationship(Comment)
        
    def to_add(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
