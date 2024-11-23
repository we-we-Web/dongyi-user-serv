from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.auth_controller import router as auth_router
from api.account_controller import router as account_router
from infrastructure.database import init_db

if __name__ == "__main__":
    init_db()
    print("資料表已成功初始化")

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
app.include_router(account_router, prefix='/account', tags=["Account"])