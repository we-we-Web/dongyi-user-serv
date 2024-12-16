from fastapi import APIRouter, Depends, HTTPException
from usecases.account_usecase import AccountUseCase
from repository.account_repo_impl import AccountRepositoryImpl
from infrastructure.database import get_db
from domain.account_entity import AccountEntity
from api.dto.account_request import GetAccountRequest, AddOrderRequest

router = APIRouter()

@router.get("/")
def get_demo(): 
    return "hello account service in fastapi"

@router.post("/account-get")
def get_account(request: GetAccountRequest, db=Depends(get_db)):
    try:
        account_repository = AccountRepositoryImpl(db)
        account_usecase = AccountUseCase(account_repository)
        account = account_usecase.get_account(request.id)
        return account.model_dump()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/account-create")
def create_account(account: AccountEntity, db=Depends(get_db)):
    try:
        account_repository = AccountRepositoryImpl(db)
        account_usecase = AccountUseCase(account_repository)
        new_account = account_usecase.create_account(account)
        return {"account": new_account.model_dump()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.patch("/order-add")
def add_order(request: AddOrderRequest, db=Depends(get_db)):
    try:
        account_repository = AccountRepositoryImpl(db)
        account_usecase = AccountUseCase(account_repository)
        account_usecase.add_order(request.id, request.order)
        return {"message": f"the order {request.order} added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))