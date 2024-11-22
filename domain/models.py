from pydantic import BaseModel

class OAuthToken(BaseModel):
    code: str

class GoogleAuthResponse(BaseModel):
    id_token: str