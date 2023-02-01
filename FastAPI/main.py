import logging
from sqlalchemy.orm import Session
from database.db_config import SessionLocal, engine
from typing import List
from fastapi import Depends, FastAPI, HTTPException

logging.basicConfig()  # 쿼리 로그를 남기기

logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO) 

app = FastAPI()

def get_db() :
    db = SessionLocal()
    
    try : 
        yield db # 비동기 프로그래밍 
        
    finally :
        db.close() # db닫음
        
@app.post("/post/" , )








