from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()

class User(BaseModel):
    id:int
    name:str
    city:str
    status:bool

user_details=[]
@app.get("/")
def get_details():
    return{
        "message":"Welcom to the New World!"
    }
@app.post("/user")
def create_user(user:User):
    user_details.append(user)
    return{
        "message":"Data inseted successfully...",
        "result":user_details
    }


