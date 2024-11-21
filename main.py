from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.auth_router import router as auth_router

app = FastAPI()

access_origin=[
    "http://localhost:3000", 
    "https://dongyi.hnd1.zeabur.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=access_origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth",  tags=["Auth"])