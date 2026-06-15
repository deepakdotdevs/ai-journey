from pydantic import BaseModel, Field
from typing import List, Literal
from pydantic_core import ValidationError

class Message(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str = Field(min_length=1)

class LLMRequest(BaseModel):
    model: Literal["gpt-4", "claude-3"]

    max_tokes: int = Field(
        ge = 100,
        le= 4000,
        description = "Must be b/w 100 and 4000"
    )

    temperature: float = Field(
        ge = 0.0,
        le = 2.0,
        description = "Must be b/w 0.0 and 2.0"
    )

    messages: List[Message]

# vaild request

try:
    request = LLMRequest(
        model="gpt-4",
        max_tokes=1000,
        temperature=0.7,
        messages=[
            {
                "role": "user",
                "content": "Explain FastAPI in simple words."
            }
        ]
    )
    print("Valid Request")
    print(request.model_dump())

except ValidationError as e:
    print("Validation Error: ")
    print(e)

    
# Invalid Model : 

try:
    bad_request = LLMRequest(
        model="gemini",
        max_tokens=1000,
        temperature=0.7,
        messages=[
            {
                "role": "user",
                "content": "Hello"
            }
        ]
    )
except ValidationError as e:
    print("\nInvalid Model Error:")
    print(e)

# Invalid Temperature
try:
    bad_request = LLMRequest(
        model="gpt-4",
        max_tokens=1000,
        temperature=5.0,
        messages=[
            {
                "role": "user",
                "content": "Hello"
            }
        ]
    )
except ValidationError as e:
    print("\nInvalid Temperature Error:")
    print(e)

# Invalid Role
try:
    bad_request = LLMRequest(
        model="gpt-4",
        max_tokens=1000,
        temperature=0.7,
        messages=[
            {
                "role": "admin",
                "content": "Hello"
            }
        ]
    )
except ValidationError as e:
    print("\nInvalid Role Error:")
    print(e)