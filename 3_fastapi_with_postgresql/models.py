from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship

from database import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    year = Column(Integer, index=True)
    is_published = Column(Boolean, index=True)

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    std_id = Column(Integer, index=True)
    birth = Column(String, index=True)
    gender = Column(String, index=True)

class Coffee(Base):
    __tablename__ = 'coffees'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Integer, index=True)

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    coffee_id = Column(Integer, ForeignKey('coffees.id'))
    quantity = Column(Integer, index=True)
    total_price = Column(Integer, index=True)
    notes = Column(String, index=True)