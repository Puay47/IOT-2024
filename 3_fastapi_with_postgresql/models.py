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
