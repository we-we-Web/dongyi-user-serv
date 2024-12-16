from pydantic import BaseModel

class GetAccountRequest(BaseModel):
    id: str

class AddOrderRequest(BaseModel):
    id: str
    order: str