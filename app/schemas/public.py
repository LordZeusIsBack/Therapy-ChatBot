from pydantic import BaseModel, ConfigDict

from datetime import datetime


class HMACPublic(BaseModel):
    id: int
    user_identifier_hash: str

    model_config = ConfigDict(from_attributes=True)


class UserPublic(BaseModel):
    id: int

    model_config = ConfigDict(from_attributes=True)


class AuditPublic(BaseModel):
    id: int
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)


class SymptomEmbeddingPublic(BaseModel):
    id: int
    symptom: str
    intensity: float

    model_config = ConfigDict(from_attributes=True)
