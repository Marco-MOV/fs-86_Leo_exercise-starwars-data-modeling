import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Identification (Base):
    __tablename__ = 'Identification'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Characters (Base):
    __tablename__ = 'Characters'
    id = Column(Integer, primary_key=True)
    birth_year = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    homeworld = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    identification_id = Column(Integer, ForeignKey('identification.id'))
    identification = relationship(Identification)

class Planets (Base):
    __tablename__ = 'Planets'
    id = Column(Integer, primary_key=True)
    terrain = Column(String(250), nullable=False)
    surface_wate = Column(String(250), nullable=False)
    diameter = Column(String(250), nullable=False)
    rotation_period= Column(String(250), nullable=False)
    orbital_period = Column(String(250), nullable=False)
    identification_id = Column(Integer, ForeignKey('identification.id'))
    identification = relationship(Identification)

class Starships(Base):
    __tablename__ = 'Starships'
    id = Column(Integer, primary_key=True)
    model = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    length = Column(String(250), nullable=False)
    passengers = Column(String(250), nullable=False)
    crew = Column(String(250), nullable=False)
    identification_id = Column(Integer, ForeignKey('identification.id'))
    identification = relationship(Identification)

class Favorites(Base):
    __tablename__ = 'Favorites'
    id = Column(Integer, primary_key=True)
    identification_id = Column(Integer, ForeignKey('identification.id'))
    identification = relationship(Identification)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
