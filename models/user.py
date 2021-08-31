import sys
sys.path.insert(0, "C:\\Users\\chengyi0818\\repos\\pf_sign")
from sqlalchemy import Column, Integer, String, Text, Date, DateTime, ForeignKey, UniqueConstraint, Index
from sqlalchemy import create_engine
from common.db.base import BaseMixedIn, Base
from sqlalchemy.orm import sessionmaker


class PFGroupInfo(Base, BaseMixedIn):
    __tablename__ = 'pf_group_info'
    group_name = Column(String)


class PFUserInfo(Base, BaseMixedIn):
    __tablename__ = 'pf_user_info'
    nick_name = Column(String)
    secret_info_id = Column(Integer)
    group_id = Column(Integer)
    
    
class PFUserSecretInfo(Base, BaseMixedIn):
    __tablename__ = 'pf_user_secret_info'
    username =  Column(String)
    password = Column(String)
    salt = Column(String)

if __name__ == '__main__':
    import hashlib
    hashlib.md5("18071228salt".encode('utf-8')).hexdigest()

    from common.db.base import engine
    SessionFactory = sessionmaker(bind=engine)
    session = SessionFactory()
    group = PFGroupInfo()
    group.group_name = '测试租户2'
    session.add(group)
    session.commit()