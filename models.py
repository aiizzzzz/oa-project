# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 17:47:10 2026

@author: hp
"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from database import Base
import datetime

class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    parent_id = Column(Integer, nullable=True)
    sort = Column(Integer, default=1)
    create_time = Column(DateTime, default=datetime.datetime.now)

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(100))
    phone = Column(String(20))
    position_id = Column(Integer)
    department_id = Column(Integer, ForeignKey("departments.id"))
    status = Column(Integer, default=1)
    entry_date = Column(String(20))
    gender = Column(Integer)
    create_time = Column(DateTime, default=datetime.datetime.now)
    update_time = Column(DateTime, default=datetime.datetime.now)