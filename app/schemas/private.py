from pydantic import BaseModel, ConfigDict

from datetime import datetime

class HMACInternal(BaseModel):
    id: int
    user_identifier_hash: str
    salt: str
    hmac_key: str

    model_config = ConfigDict(from_attributes=True)


class UserInternal(BaseModel):
    id: int
    hmac_id: int
    encrypted_name: str
    encrypted_email: str
    encrypted_dob: str | None = None

    model_config = ConfigDict(from_attributes=True)


class AuditInternal(BaseModel):
    id: int
    user_hmac_id: int
    timestamp: datetime
    chat_log: str | None = None

    model_config = ConfigDict(from_attributes=True)


class SymptomEmbeddingInternal(BaseModel):
    id: int
    user_hmac_id: int
    symptom: str
    intensity: float
    embedding: list[float] | None = None

    model_config = ConfigDict(from_attributes=True)
