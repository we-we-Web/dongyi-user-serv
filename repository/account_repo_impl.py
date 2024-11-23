from typing import Optional
from sqlalchemy.orm import Session
from domain.account_entity import AccountEntity
from repository.account_repository import AccountRepository
from domain.models import Account
from datetime import datetime, timezone


class AccountRepositoryImpl(AccountRepository):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def find_by_id(self, id: str) -> Optional[AccountEntity]:
        account = self.db_session.query(Account).filter_by(id=id).first()
        if account:
            return AccountEntity(
                id=account.id,
                name=account.name,
                cart=account.cart,
                orders=account.orders,
                created_at=str(account.created_at),
                updated_at=str(account.updated_at)
            )
        return None

    def create_account(self, account: AccountEntity) -> AccountEntity:
        new_account = Account(
            id=account.id,
            name=account.name,
            cart=account.cart,
            orders=account.orders if account.orders else [],
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )
        self.db_session.add(new_account)
        self.db_session.commit()
        self.db_session.refresh(new_account)
        return AccountEntity(
            id=new_account.id,
            name=new_account.name,
            cart=new_account.cart,
            orders=new_account.orders,
            created_at=str(new_account.created_at),
            updated_at=str(new_account.updated_at)
        )

    def update_cart(self, id: str, cart: str) -> None:
        account = self.db_session.query(Account).filter_by(id=id).first()
        if account:
            account.cart = cart
            self.db_session.commit()

    def add_order(self, id: str, order_id: str) -> None:
        account = self.db_session.query(Account).filter_by(id=id).first()
        if account:
            account.orders.append(order_id)
            self.db_session.commit()