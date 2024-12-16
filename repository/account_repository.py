from abc import ABC, abstractmethod
from typing import Optional
from domain.account_entity import AccountEntity

class AccountRepository(ABC):
    @abstractmethod
    def find_by_id(self, id: str) -> Optional[AccountEntity]:
        pass

    @abstractmethod
    def create_account(self, account: AccountEntity) -> AccountEntity:
        pass

    @abstractmethod
    def add_order(self, id: str, order_id: str) -> None:
        pass