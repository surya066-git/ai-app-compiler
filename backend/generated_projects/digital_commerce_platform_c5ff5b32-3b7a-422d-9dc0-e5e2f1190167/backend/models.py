from sqlalchemy import Column, DateTime, Integer, String, func
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    status = Column(String, default='active')
    description = Column(String, default='')
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Cart(Base):
    __tablename__ = 'carts'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    status = Column(String, default='active')
    description = Column(String, default='')
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    status = Column(String, default='active')
    description = Column(String, default='')
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Payment(Base):
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    status = Column(String, default='active')
    description = Column(String, default='')
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    status = Column(String, default='active')
    description = Column(String, default='')
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Campaign(Base):
    __tablename__ = 'campaigns'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    status = Column(String, default='active')
    description = Column(String, default='')
    created_at = Column(DateTime(timezone=True), server_default=func.now())
