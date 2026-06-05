from sqlalchemy import Column, DateTime, Integer, String, func
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Lead(Base):
    __tablename__ = 'leads'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    status = Column(String, default='active')
    description = Column(String, default='')
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Propertie(Base):
    __tablename__ = 'properties'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    status = Column(String, default='active')
    description = Column(String, default='')
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Agent(Base):
    __tablename__ = 'agents'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    status = Column(String, default='active')
    description = Column(String, default='')
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Metric(Base):
    __tablename__ = 'metrics'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    status = Column(String, default='active')
    description = Column(String, default='')
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Report(Base):
    __tablename__ = 'reports'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    status = Column(String, default='active')
    description = Column(String, default='')
    created_at = Column(DateTime(timezone=True), server_default=func.now())
