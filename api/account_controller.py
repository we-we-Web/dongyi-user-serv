from fastapi import APIRouter, Depends, HTTPException
from usecases.account_usecase import AccountUseCase
from repository.account_repo_impl import AccountRepositoryImpl
from infrastructure.database import get_db
from domain.account_entity import AccountEntity
from api.dto.account_request import GetAccountRequest, AddOrderRequest, UpdateNameRequest, UpdateLiked, OTPCode

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
def create_account(otpCode: OTPCode, db=Depends(get_db)):
    try:
        account_repository = AccountRepositoryImpl(db)
        account_usecase = AccountUseCase(account_repository)
        new_account = account_usecase.create_account(otpCode.OTP)
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

@router.patch("/name-update")
def update_name(request: UpdateNameRequest, db=Depends(get_db)):
    try:
        account_repository = AccountRepositoryImpl(db)
        account_usecase = AccountUseCase(account_repository)
        account_usecase.update_name(request.id, request.name)
        return {"message": f"the name updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.delete("/account-delete")
def delete_account(request: GetAccountRequest, db=Depends(get_db)):
    try:
        account_repository = AccountRepositoryImpl(db)
        account_usecase = AccountUseCase(account_repository)
        account_usecase.delete_account(request.id)
        return {"message": f"the account {request.id} deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.patch("/liked-update")
def update_liked(request: UpdateLiked, db=Depends(get_db)):
    try:
        account_repository = AccountRepositoryImpl(db)
        account_usecase = AccountUseCase(account_repository)
        account_usecase.update_liked(request.id, request.liked)
        return {"message": f"the liked updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/isAdmin/{id}")
def is_admin(id: str, db=Depends(get_db)):
    try:
        account_repository = AccountRepositoryImpl(db)
        account_usecase = AccountUseCase(account_repository)
        is_admin = account_usecase.is_admin(id)
        return is_admin
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/otp-send")
async def send_otp(request: AccountEntity, db=Depends(get_db)):
    try:
        account = AccountRepositoryImpl(db)
        account_usecase = AccountUseCase(account)
        status = await account_usecase.send_otp(request)
        return {"message": f"{status}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
