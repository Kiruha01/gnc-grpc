import os

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()

# create database engine
engine = create_engine(os.environ.get("DB_URL"), echo=True)

# create a session factory
Session = sessionmaker(bind=engine)

# create base class for models
Base = declarative_base()

# define Item model
class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    def __repr__(self):
        return f"<Item(id={self.id}, name={self.name}, description={self.description})>"

# create database schema
Base.metadata.create_all(engine)