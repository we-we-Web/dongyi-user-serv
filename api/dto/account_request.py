from pydantic import BaseModel

class GetAccountRequest(BaseModel):
    id: str

class AddOrderRequest(BaseModel):
    id: str
    order: str

class UpdateNameRequest(BaseModel):
    id: str
    name: str

class UpdateLiked(BaseModel):
    id: str
    liked: int

class OTPCode(BaseModel):
    OTP: str

class CreateAccountRequest(BaseModel):
    OTP: str
    email: str