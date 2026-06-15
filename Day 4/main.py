from pydantic import BaseModel, Field, field_validator
from typing import Optional, List

class Address(BaseModel):
    city: str
    pincode: str = Field(min_length=6, max_length=6)

class UserProfile(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(ge=1, le=120)
    email: str
    skills: List[str] = []
    address: Optional[Address]= None

    @field_validator("email")
    @classmethod
    def email_must_have_at(cls, v):
        if '@' not in v:
            raise ValueError("Not a valid email")
        return v
    
user = UserProfile(
    name="Deepak", age = 20,
    email = "deepak@gmail.com",
    skills = ["Python", "FastAPI"],
    address = {"city":"Sonipat", "pincode":"133254"}
)
print(user.model_dump()) # model_dump -> Converts objects into dictionary
