from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, TIMESTAMP, text, func

Base = declarative_base()

class BaseMixedIn(object):
    id = Column(Integer, primary_key=True, comment='id')
    create_time = Column(TIMESTAMP, server_default=func.now(), comment='创建时间')
    update_time = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), comment='更新时间')

def create_all():
    engine = create_engine(
         "mysql+pymysql://root:123@localhost:3306/pf_base?charset=utf8",
         max_overflow=0,  # 超过连接池大小外最多创建的连接
         pool_size=5,  # 连接池大小
         pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
         pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
     )
    Base.metadata.create_all(engine)

engine = create_engine(
         "mysql+pymysql://root:123@localhost:3306/pf_base?charset=utf8",
         max_overflow=0,  # 超过连接池大小外最多创建的连接
         pool_size=5,  # 连接池大小
         pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
         pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
     )

if __name__ == '__main__':
    create_all()