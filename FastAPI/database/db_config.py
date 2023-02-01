# 완성본 건드리지마시오

import pickle 

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

with open('db_dict.pickle','rb') as f :
    db_info = pickle.load(f)
    

class DB_setting : 
    
    DB_USERNAME : str = db_info.get("DB_USERNAME")
    DB_PASSWORD = db_info.get("DB_PASSWORD")
    DB_HOST : str = db_info.get("DB_HOST","localhost")
    DB_PORT : str = db_info.get("DB_PORT",3306)
    DB_DATABASE : str = db_info.get("DB_DATABASE")
	
    DB_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    
# 연결 제어 (like 소통창구!!)
engine = create_engine(DB_setting())

# sessionmaker : db와 소통하기 위한 절차
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
# auto* : 자동으로 올라가는것 방지!
# flush : 변경사항 전송
# commit : 변경사항 적용, 저장

# 객체 테이블로 매핑하는 ORM model
Base = declarative_base()