from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship

from db import engine

class Base(DeclarativeBase):
    pass

class Owner(Base):
    __tablename__ = "owners"
    id = Column(Integer, primary_key=True)
    fullname = Column(String(150))
    email = Column(String(150), unique=True)


class Cat(Base):
    __tablename__ = "cats"
    id = Column(Integer, primary_key=True)
    nick = Column(String)
    age = Column(Integer)
    vaccinated = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("owners.id"), nullable=False)
    owner = relationship("Owner", backref="cats")

Base.metadata.create_all(bind=engine)



