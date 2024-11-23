from fastapi import APIRouter, HTTPException
from usecases.auth_usecase import GoogleAuthUseCase
from repository.auth_repository import GoogleAuthRepository
from domain.models import OAuthToken

router = APIRouter()
google_auth_repo = GoogleAuthRepository()
google_auth_usecase = GoogleAuthUseCase(google_auth_repo)


@router.get("/login")
def auth_google():
    try:
        auth_url = google_auth_usecase.generate_auth_url()
        return {"auth_url": auth_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/callback")
def auth_google_callback(token: OAuthToken):
    try:
        google_response = google_auth_usecase.handle_callback(token.code)
        return google_response
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))