from pydantic import BaseModel, ConfigDict


class HMACPublic(BaseModel):
    id: int
    user_identifier_hash: str

    model_config = ConfigDict(from_attributes=True)


class UserPublic(BaseModel):
    id: int

    model_config = ConfigDict(from_attributes=True)
