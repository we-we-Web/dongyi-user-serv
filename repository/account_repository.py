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

    @abstractmethod
    def update_name(self, id: str, name: str) -> None:
        pass

    @abstractmethod
    def delete_account(self, id: str) -> None:
        pass

    @abstractmethod
    def update_liked(self, id: str, liked_id: int) -> None:
        pass

    @abstractmethod
    def is_admin(self, id: str) -> bool:
        pass

    @abstractmethod
    async def send_otp(self, id: str) -> str:
        pass