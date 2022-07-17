import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastame = Column(String(250), nullable=False)
    email = Column(String(250), unique=True)
    password = Column(String(250), nullable=False)
    phone_number = Column(String(20), nullable=False)
    user_name = Column(String(20), unique=True)



    def login(self):
        return{}

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    date = Column(DateTime)
    tag = Column(String(250), nullable=True)
    likes = Column(Integer)
    comments = Column(String(250), nullable=True)

class DirectMessage(Base):
    __tablename__ = 'direct_message'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    date = Column(DateTime)
    



# class Planet(Base):
#     __tablename__ = 'planet'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250))
#     color = Column(String(250))
#     climate = Column(String(250))
#     population = Column(Integer)
#     rotation_period = Column(Integer)
#     orbital_period = Column(Integer)
#     diameter = Column(Integer)

class LikedPost(Base):
    __tablename__ = 'liked_post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class MessageSent(Base):
    __tablename__ = 'message_sent'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    direct_message = Column(Integer, ForeignKey('direct_message.id'))
# class FavoritePlanet(Base):
#     __tablename__ = 'favorite_planet'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('user.id'))
#     planet_id = Column(Integer, ForeignKey('planet.id'))
    
    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')