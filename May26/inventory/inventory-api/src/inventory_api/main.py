from fastapi import FastAPI, Header
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

app = FastAPI(title="Inventory API")

@app.get("/health")
def health_check():
    return {"status": "ok"}



@app.get("/users/{user_id}")
async def get_user(user_id: int):
    """This api will return user information
    """
    print(f"fetching informaton for user with id {user_id}")
    return {
        "id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

@app.get("/products/")
async def get_products(category:str, limit:int = 10):
    return {
        "category": category,
        "limit": limit
    }


@app.get("/profile")
async def profile(authorization: str = Header(), version: str = Header(default='v1')):
    return { 
        "recieved_token": authorization,
        "version": version
    }

@app.post("/users")
async def create_user(user: User) -> User:
    return user
