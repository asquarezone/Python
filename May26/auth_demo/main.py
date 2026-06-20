from fastapi import FastAPI, Depends, HTTPException,status
from typing import Annotated

from fastapi.security import HTTPBasic, HTTPBasicCredentials


app = FastAPI(title="fastapi authentication demo")
security = HTTPBasic()

def verify_credentials(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    username="admin"
    password="admin@123"
    if credentials.username == username and credentials.password == password:
        # right Credentials
        return {
            "name": "khaja",
            "email": "test@test.com",
            "mobile": "99999999999",
            "address": "xxxxxxxxxxxxxxxxxxxxxxxxxxx"
        }
    raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"}, # Required by 401 spec
        )



@app.get("/public")
def get_general_info():
    return {
        "title": "FastApi Authentication Demo",
        "description": "learning to build apis"
    }

@app.get("/details")
def get_details(username:str = Depends(verify_credentials)):
    return {
        "message": "everything looks good"
    }


@app.post("/me")
def get_profile(username:str = Depends(verify_credentials)):

    return {
        "name": "khaja",
        "email": "test@test.com",
        "mobile": "99999999999",
        "address": "xxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }

