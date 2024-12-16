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

    def create_account(self, account: AccountEntity) -> AccountEntity:
        return self.account_repository.create_account(account)

    def update_cart(self, id: str, cart: list) -> None:
        self.account_repository.update_cart(id, cart)

    def add_order(self, id: str, order_id: str) -> None:
        self.account_repository.add_order(id, order_id)

    def update_name(self, id: str, name: str) -> None:
        self.account_repository.update_name(id, name)