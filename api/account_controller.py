from fastapi import APIRouter, Depends, HTTPException
from usecases.account_usecase import AccountUseCase
from repository.account_repo_impl import AccountRepositoryImpl
from infrastructure.database import get_db
from domain.account_entity import AccountEntity

router = APIRouter()

@router.get("/")
def get_demo(): 
    return "hello account entity in fastapi"

@router.get("/{id}")
def get_account(id: str, db=Depends(get_db)):
    try:
        account_repository = AccountRepositoryImpl(db)
        account_usecase = AccountUseCase(account_repository)
        account = account_usecase.get_account(id)
        return {"account": account.model_dump()}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/")
def create_account(account: AccountEntity, db=Depends(get_db)):
    try:
        account_repository = AccountRepositoryImpl(db)
        account_usecase = AccountUseCase(account_repository)
        new_account = account_usecase.create_account(account)
        return {"account": new_account.model_dump()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{id}/cart")
def update_cart(id: str, cart: list, db=Depends(get_db)):
    try:
        account_repository = AccountRepositoryImpl(db)
        account_usecase = AccountUseCase(account_repository)
        account_usecase.update_cart(id, cart)
        return {"message": "Cart updated"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/{id}/order")
def add_order(id: str, order_id: str, db=Depends(get_db)):
    try:
        account_repository = AccountRepositoryImpl(db)
        account_usecase = AccountUseCase(account_repository)
        account_usecase.add_order(id, order_id)
        return {"message": "Order added"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))