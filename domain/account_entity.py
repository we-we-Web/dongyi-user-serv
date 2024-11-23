from pydantic import BaseModel
from typing import List, Optional

class AccountEntity(BaseModel):
    id: str # email
    name: str
    cart: Optional[str] = None
    orders: Optional[List[str]] = []
    created_at: Optional[str] = None
    updated_at: Optional[str] = None