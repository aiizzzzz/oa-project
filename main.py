# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 21:01:33 2026

@author: hp
"""
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, get_db, Base

app = FastAPI(title="OA系统", version="1.0")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "OA系统启动成功"}