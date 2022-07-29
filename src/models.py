import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    UserId = Column(Integer, primary_key=True)
    Name = Column(String(250), nullable=False)
    Email = Column(String(250), nullable=False)
    Address = Column(String(250), nullable=False)
    Pasword = Column(String(250), nullable=False)

class Peoplefavoritos(Base):
    __tablename__ = 'Peoplefavoritos'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    UserId = Column(Integer, ForeignKey('User.UserId'), primary_key=True, )
    PeopleId = Column(String(250), nullable=False)

class Planetfavoritos(Base):
    __tablename__ = 'Planetfavoritos'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    UserId = Column(Integer, ForeignKey('User.UserId'), primary_key=True, )
    PlanetId = Column(String(250), nullable=False)

class Vehiclesfavoritos(Base):
    __tablename__ = 'Vehiclesfavoritos'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    UserId = Column(Integer, ForeignKey('User.UserId'), primary_key=True, )
    VehiclesId = Column(String(250), nullable=False)

class People(Base):
    __tablename__ = 'People'
    PeopleId = Column(Integer, ForeignKey('Peoplefavoritos.UserId'), primary_key=True,)
    Name = Column(String(250))
    Birthday = Column(String(250))
    Gender = Column(String(250), nullable=False)
    Height = Column(String(250))
    Skin_color = Column(String(250))
    Eye_color = Column(String(250))

class Planets(Base):
    __tablename__ = 'Planets'
    PlanetId = Column(Integer, ForeignKey('Planetfavoritos.UserId'), primary_key=True,)
    Name = Column(String(250))
    Population = Column(String(250))
    Climate = Column(String(250), nullable=False)
    Terrain = Column(Integer, ForeignKey('person.id'))
    Rotation_period = Column(String(250))
    Orbital_period = Column(String(250))

class Vehicles(Base):
    __tablename__ = 'Vehicles'
    VehiclesId = Column(Integer, ForeignKey('Vehiclesfavoritos.UserId'), primary_key=True,)
    Name = Column(String(250))
    Model = Column(String(250))
    Vehicles_class = Column(String(250), nullable=False)
    Length = Column(Integer, ForeignKey('person.id'))
    Cargo_capacity = Column(String(250))
    Max_Speed = Column(String(250))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')