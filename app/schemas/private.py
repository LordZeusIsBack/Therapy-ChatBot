from pydantic import BaseModel, ConfigDict


class HMACInternal(BaseModel):
    id: int
    user_identifier_hash: str
    salt: str
    hmac_key: str

    model_config = ConfigDict(from_attributes=True)
