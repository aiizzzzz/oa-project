# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 21:01:33 2026

@author: hp
"""
from fastapi import FastAPI
from database import engine, Base
import models

app = FastAPI(title="OA系统", version="1.0")
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "OA系统启动成功"}