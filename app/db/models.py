from pgvector.sqlalchemy import VECTOR
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, Text, Float
from sqlalchemy.orm import relationship

from database import Base


class HMACTable(Base):
    __tablename__ = 'hmac_keys'

    id = Column(Integer, primary_key=True, index=True)
    user_identifier_hash = Column(String, unique=True, index=True, nullable=False)
    salt = Column(String, nullable=False)
    hmac_key = Column(String, nullable=False)
    user = relationship('User', back_populates='hmac', uselist=False)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    hmac_id = Column(Integer, ForeignKey('hmac_keys.id'), unique=True, nullable=False)
    encrypted_name = Column(String, nullable=False)
    encrypted_email = Column(String, nullable=False)
    encrypted_dob = Column(String)

    hmac = relationship('HMACTable', back_populates='user')

class Audit(Base):
    __tablename__ = 'audit_logs'

    id = Column(Integer, primary_key=True, index=True)
    user_hmac_id = Column(Integer, ForeignKey("hmac_keys.id"))
    timestamp = Column(DateTime(timezone=True), default=func.now())
    chat_log = Column(Text)

    hmac = relationship('HMACTable')


class SymptomEmbedding(Base):
    __tablename__ = 'symptom_embeddings'

    id = Column(Integer, primary_key=True, index=True)
    user_hmac_id = Column(Integer, ForeignKey('hmac_keys.id'), nullable=False)
    symptom = Column(String, nullable=False)
    intensity = Column(Float, default=0.0)
    embedding = Column(VECTOR(384))

    hmac = relationship('HMACTable')
