from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional
import re


class UserCreateSchema(BaseModel):
    '''
    Schema for creating a new user.
    Attributes:
        email (EmailStr): User's email address.
        first_name (str): User's first name.
        last_name (str): User's last name.
        password (str): User's password.
    Raises:
        ValueError: If the password is not valid.
    '''
    email: EmailStr = Field(..., description="User's email address")
    first_name: str = Field(..., description="User's first name")
    last_name: str = Field(..., description="User's last name")
    password: str = Field(..., description="User's password")

    # Password strength validator
    @field_validator("password")
    def validate_password(cls, v):
        # 8 chars + uppercase + lowercase + number
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not re.search("[A-Z]", v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search("[a-z]", v):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search("[0-9]", v):
            raise ValueError("Password must contain at least one number")
        return v

class UserUpdateSchema(BaseModel):
    '''
    Schema for updating a user.
    Attributes:
        email (EmailStr): User's email address (optional).
        first_name (str): User's first name (optional).
        last_name (str): User's last name (optional).
        disabled (bool): User's status (optional).
    '''
    email: Optional[EmailStr] = Field(None, description="User's email address (optional)")
    first_name: Optional[str] = Field(None, description="User's first name (optional)")
    last_name: Optional[str] = Field(None, description="User's last name (optional)")
    disabled: Optional[bool] = Field(None, description="User's status (optional)")

class UserSchema(BaseModel):
    id: str
    email: EmailStr
    first_name: str
    last_name: str
    disabled: bool | None = None