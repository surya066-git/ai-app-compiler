from sqlalchemy import Column, DateTime, Integer, String, func
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Contact(Base):
    __tablename__ = 'contacts'
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

class Analytic(Base):
    __tablename__ = 'analytics'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    status = Column(String, default='active')
    description = Column(String, default='')
    created_at = Column(DateTime(timezone=True), server_default=func.now())
