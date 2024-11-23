from pydantic import BaseModel
from sqlalchemy import Column, JSON, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class OAuthToken(BaseModel):
    code: str

class GoogleAuthResponse(BaseModel):
    id_token: str

class Account(Base):
    __tablename__ = 'accounts'  # 資料表名稱

    id = Column(String(255), primary_key=True, unique=True, autoincrement=False)
    name = Column(String(255), nullable=True)
    cart = Column(String(255), nullable=True)
    orders = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    def __repr__(self):
        return f"<Account(id={self.id}, name={self.name}, cart={self.cart}, orders={self.orders})>)>"