from repository.account_repository import AccountRepository
from domain.account_entity import AccountEntity

class AccountUseCase:
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def get_account(self, id: str) -> AccountEntity:
        account = self.account_repository.find_by_id(id)
        if not account:
            raise ValueError("Account not found")
        return account

    def create_account(self, otp: str) -> str:
        return self.account_repository.create_account(otp)

    def add_order(self, id: str, order_id: str) -> None:
        self.account_repository.add_order(id, order_id)

    def update_name(self, id: str, name: str) -> None:
        self.account_repository.update_name(id, name)

    def delete_account(self, id: str) -> None:
        self.account_repository.delete_account(id)

    def update_liked(self, id: str, liked_id: int) -> None:
        self.account_repository.update_liked(id, liked_id)

    def is_admin(self, id: str) -> bool:
        return(self.account_repository.is_admin(id))
    
    def send_otp(self, id: str) -> str:
        return(self.account_repository.send_otp(id))