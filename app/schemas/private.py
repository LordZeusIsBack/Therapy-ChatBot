from pydantic import BaseModel, ConfigDict


class HMACInternal(BaseModel):
    id: int
    user_identifier_hash: str
    salt: str
    hmac_key: str

    model_config = ConfigDict(from_attributes=True)


class UserInternal(BaseModel):
    id: int
    hmac_id: str
    encrypted_name: str
    encrypted_email: str
    encrypted_dob: str | None = None

    model_config = ConfigDict(from_attributes=True)
