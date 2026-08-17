from pydantic import BaseModel, Field, EmailStr, HttpUrl, UUID4


class UserRequest(BaseModel):
    name: str = Field(..., example="Rahul")
    age: int = Field(..., example=23)
    email: EmailStr
    website: HttpUrl | None = None


class UserResponse(UserRequest):
    id: UUID4