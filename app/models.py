from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from sqlalchemy import create_engine

Base = declarative_base()

DATABASE_URL = "sqlite:///./wallet_logs.db"
engine = create_engine(DATABASE_URL)


class WalletLog(Base):
    __tablename__ = "wallet_logs"
    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, nullable=False)
    balance = Column(String, nullable=False)
    bandwidth = Column(Integer, nullable=False)
    energy = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


Base.metadata.create_all(engine)


def get_db():
    with Session(engine) as session:
        yield session
