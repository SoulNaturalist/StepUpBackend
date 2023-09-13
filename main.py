from db import *
from models import *
from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware


origins = [
    "http://localhost",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/login", status_code=200)
async def login_endpoint(login_data: LoginUserData,response: Response):
    exist_user = await get_user_by_email(login_data.email)
    if exist_user:
        valid_password = bcrypt.checkpw(login_data.password.encode('utf-8'), exist_user[0][3].encode('utf-8'))
        if valid_password:
            response.set_cookie(key="jwt", value="there will be a token here soon.")
            return {"message": "Good, welcome!"}
        return {"message": "Bad credentials"}
    response.status_code = status.HTTP_400_BAD_REQUEST
    return {"message": "User not found"}

@app.post("/register", status_code=201)
async def register_endpoint(user_data: UserData):
    message_dict = {True:"User registered", False:"User not registered", None:"User not registered"}
    created = await create_user(user_data.name, user_data.password, user_data.email)
    return {"message": message_dict[bool(created)]}