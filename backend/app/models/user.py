import uuid

from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel

# Import Item to resolve forward reference without future annotations
from .item import Item


# Database model only
class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    is_active: bool = True
    is_superuser: bool = False
    full_name: str | None = Field(default=None, max_length=255)
    phone_number: str | None = Field(default=None, max_length=20)
    username: str | None = Field(default=None, unique=True, index=True, max_length=50)
    hashed_password: str
    items: list[Item] = Relationship(back_populates="owner", cascade_delete=True)