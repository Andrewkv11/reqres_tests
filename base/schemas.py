from pydantic import BaseModel
from pydantic.types import List


class User(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class UsersList(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[User]


class UserSingle(BaseModel):
    data: User


class UserCreate(BaseModel):
    name: str
    job: str
    id: str
    createdAt: str


class UserUpdate(BaseModel):
    name: str
    job: str
    updatedAt: str


class UserUpdatePart(BaseModel):
    name: str
    job: str
    updatedAt: str


class UserRegister(BaseModel):
    id: str
    token: str


class UserRegisterUnsuccessful(BaseModel):
    error: str


class UserLogin(BaseModel):
    token: str


class UserLoginUnsuccessful(BaseModel):
    error: str


class Resource(BaseModel):
    id: int
    name: str
    year: int
    color: str
    pantone_value: str


class ResourceList(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[Resource]


class ResourceSingle(BaseModel):
    data: Resource
