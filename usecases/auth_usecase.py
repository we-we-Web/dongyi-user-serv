from typing import Optional
from domain.models import GoogleAuthResponse
from repository.auth_repository import GoogleAuthRepository

class GoogleAuthUseCase:
    def __init__(self, google_auth_repo: GoogleAuthRepository):
        self.google_auth_repo = google_auth_repo

    def generate_auth_url(self) -> str:
        return self.google_auth_repo.get_auth_url()

    def handle_callback(self, code: str) -> GoogleAuthResponse:
        id_token = self.google_auth_repo.exchange_code_for_token(code)
        if not id_token:
            raise ValueError("Failed to retrieve ID token")
        return GoogleAuthResponse(id_token=id_token)