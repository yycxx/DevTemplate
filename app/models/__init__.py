from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(engine)
# 创建对象的基类:
Base = declarative_base()
# 创建所有表
Base.metadata.create_all(engine)
