from typing import Optional
from sqlalchemy.orm import Session
from domain.account_entity import AccountEntity
from repository.account_repository import AccountRepository
from domain.models import Account
from datetime import datetime, timezone
from infrastructure.mongoDB import collection
from api.dto.account_request import UpdateNameRequest, CreateAccountRequest
import aiosmtplib
import os
from dotenv import load_dotenv
import pyotp
import time

load_dotenv()


class AccountRepositoryImpl(AccountRepository):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def find_by_id(self, id: str) -> Optional[AccountEntity]:
        account = self.db_session.query(Account).filter_by(id=id).first()
        if account:
            return AccountEntity(
                id=account.id,
                name=account.name,
                orders=account.orders,
                created_at=str(account.created_at),
                updated_at=str(account.updated_at)
            )
        return None

    def create_account(self, info: CreateAccountRequest) -> str:
        account = collection.find_one({"otp": info.OTP})
        if account["email"] == info.email:
            collection.delete_one({"otp": info.OTP})
            new_account = Account(
                id=account["email"],
                name=account["name"],
                orders=[],
                created_at=datetime.now(timezone.utc),
                updated_at=datetime.now(timezone.utc),
                liked=[],
            )
            self.db_session.add(new_account)
            self.db_session.commit()
            self.db_session.refresh(new_account)
            return f"Account {new_account.id} created successfully"
        else:
            return "Account creation failed"
        


    def add_order(self, id: str, order_id: str) -> None:
        account = self.db_session.query(Account).filter_by(id=id).first()
        if account:
            account.orders = account.orders + [order_id]
            self.db_session.commit()
            print(account.orders)

    def update_name(self, id, name):
        account = self.db_session.query(Account).filter_by(id=id).first()
        if account:
            account.name = name
            self.db_session.commit()

    def delete_account(self, id):
        account = self.db_session.query(Account).filter_by(id=id).first()
        if account:
            self.db_session.delete(account)
            self.db_session.commit()

    def update_liked(self, id, liked_id):
        account = self.db_session.query(Account).filter_by(id=id).first()
        if account:
            if liked_id not in account.liked:
                account.liked = account.liked + [liked_id]
                self.db_session.commit()
            elif liked_id in account.liked:
                account.liked = [id for id in account.liked if id != liked_id]
                self.db_session.commit()

    def is_admin(self, id):
        if id == os.getenv("admin_email1") or id == os.getenv("admin_email2"):
            return True
        return False
    
    async def send_otp(self, account: UpdateNameRequest):
        try:
            otp = pyotp.TOTP(pyotp.random_base32()).now()
            message = f"Subject: OTP\n\nYour OTP is {otp}. It will expire in 5 minutes."
            await aiosmtplib.send(
                message,
                sender=os.getenv("email"),
                recipients=[account.id],
                hostname=os.getenv("smtp_server"),
                port=os.getenv("smtp_port"),
                username=os.getenv("email"),
                password=os.getenv("email_password"),
                use_tls=True,
            )
            collection.update_one(
                {
                    "email": account.id,
                    "name": account.name,
                },
                {
                    "$set": {
                        "otp": otp,
                        "timestamp": datetime.now(timezone.utc),
                    }
                },
                upsert=True,
            )
            
            return "success"
        except Exception as e:
            return str(e)
        
    def get_favorites(self, id):
        account = self.db_session.query(Account).filter_by(id=id).first()
        if account:
            return account.liked
        raise ValueError("Account not found")

