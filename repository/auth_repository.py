import os
import requests
from typing import Optional

class GoogleAuthRepository:
    def __init__(self):
        self.client_id = os.getenv("GOOGLE_CLIENT_ID")
        self.client_secret = os.getenv("GOOGLE_CLIENT_SECRET")
        self.redirect_uri = os.getenv("OAUTH_REDIRECT_URL")

    def get_auth_url(self) -> str:
        return (
            "https://accounts.google.com/o/oauth2/auth?"
            f"client_id={self.client_id}&"
            f"redirect_uri={self.redirect_uri}&"
            "scope=openid%20email%20profile&"
            "response_type=code"
        )

    def exchange_code_for_token(self, code: str) -> Optional[str]:
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "code": code,
            "grant_type": "authorization_code",
            "redirect_uri": self.redirect_uri,
        }
        response = requests.post("https://oauth2.googleapis.com/token", data=data)
        if response.status_code != 200:
            return None
        return response.json().get("id_token")