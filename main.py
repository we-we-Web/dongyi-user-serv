from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import requests
import os

app = FastAPI()
load_dotenv()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://dongyi.hnd1.zeabur.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
REDIRECT_URI = "http://localhost:3000/callback"

class Token(BaseModel):
    access_token: str

@app.get("/login")
def auth_google():
    print(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET) 
    google_auth_url = (
        "https://accounts.google.com/o/oauth2/auth?"
        f"client_id={GOOGLE_CLIENT_ID}&"
        f"redirect_uri={REDIRECT_URI}&"
        "scope=openid%20email%20profile&"
        "response_type=code"
    )
    print(google_auth_url)
    return {"auth_url": google_auth_url}

@app.post("/callback")
def auth_google_callback(token: Token):
    print(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET) 
    try:
        data = {
            "client_id": GOOGLE_CLIENT_ID,
            "client_secret": GOOGLE_CLIENT_SECRET,
            "code": token.access_token,
            "grant_type": "authorization_code",
            "redirect_uri": REDIRECT_URI,
        }
        response = requests.post("https://oauth2.googleapis.com/token", data=data)
        response_data = response.json()
        id_token = response_data.get("id_token")
        return {"id_token": id_token}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Failed to authenticate")