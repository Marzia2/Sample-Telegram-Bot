import datetime
from database import Base
from sqlalchemy import String, Column, DateTime, BigInteger


class User(Base.Base):
    __tablename__ = "users"
    id = Column(BigInteger, primary_key=True, unique=True)
    username = Column(String)
    joining_date = Column(DateTime, default=datetime.datetime.utcnow)

